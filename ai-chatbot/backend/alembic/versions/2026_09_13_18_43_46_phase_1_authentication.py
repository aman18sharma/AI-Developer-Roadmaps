"""phase 1 authentication

Revision ID: 3c3f2cfbf10f
Revises:
Create Date: 2026-09-13 18:43:46.242201

"""
# pylint: disable=invalid-name
from typing import Sequence, Union

from alembic import op  # pylint: disable=no-name-in-module
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '3c3f2cfbf10f'
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None

SCHEMA = "black_and_white"


def upgrade() -> None:
    """Upgrade schema."""
    op.execute(f"CREATE SCHEMA IF NOT EXISTS {SCHEMA}")

    op.create_table(
        'users',
        sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
        sa.Column('email', sa.String(length=255), nullable=False),
        sa.Column('name', sa.String(length=100), nullable=False),
        sa.Column('hashed_password', sa.String(length=255), nullable=False),
        sa.Column('is_active', sa.Boolean(), nullable=False),
        sa.Column('created_at', sa.DateTime(), nullable=False),
        sa.PrimaryKeyConstraint('id'),
        schema=SCHEMA,
    )
    op.create_index(
        op.f('ix_users_email'), 'users', ['email'], unique=True, schema=SCHEMA
    )

    op.create_table(
        'conversations',
        sa.Column('id', sa.String(length=100), nullable=False),
        sa.Column('title', sa.String(length=255), nullable=False),
        sa.Column('created_at', sa.DateTime(), nullable=False),
        sa.Column('updated_at', sa.DateTime(), nullable=False),
        sa.Column('user_id', sa.Integer(), nullable=False),
        sa.Column('model', sa.String(length=100), nullable=False),
        sa.ForeignKeyConstraint(
            ['user_id'], [f'{SCHEMA}.users.id'], ondelete='CASCADE'
        ),
        sa.PrimaryKeyConstraint('id'),
        schema=SCHEMA,
    )
    op.create_index(
        op.f('ix_conversations_user_id'),
        'conversations',
        ['user_id'],
        unique=False,
        schema=SCHEMA,
    )

    op.create_table(
        'messages',
        sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
        sa.Column('conversation_id', sa.String(length=100), nullable=False),
        sa.Column('role', sa.String(length=20), nullable=False),
        sa.Column('content', sa.Text(), nullable=False),
        sa.Column('created_at', sa.DateTime(), nullable=False),
        sa.ForeignKeyConstraint(
            ['conversation_id'], [f'{SCHEMA}.conversations.id'], ondelete='CASCADE'
        ),
        sa.PrimaryKeyConstraint('id'),
        schema=SCHEMA,
    )
    op.create_index(
        op.f('ix_messages_conversation_id'),
        'messages',
        ['conversation_id'],
        unique=False,
        schema=SCHEMA,
    )


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_index(
        op.f('ix_messages_conversation_id'), table_name='messages', schema=SCHEMA
    )
    op.drop_table('messages', schema=SCHEMA)

    op.drop_index(
        op.f('ix_conversations_user_id'), table_name='conversations', schema=SCHEMA
    )
    op.drop_table('conversations', schema=SCHEMA)

    op.drop_index(op.f('ix_users_email'), table_name='users', schema=SCHEMA)
    op.drop_table('users', schema=SCHEMA)

    op.execute(f"DROP SCHEMA IF EXISTS {SCHEMA} CASCADE")
