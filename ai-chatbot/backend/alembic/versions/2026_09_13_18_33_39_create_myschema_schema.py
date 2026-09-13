"""create_black_and_white_schema

Revision ID: 123bca2708a4
Revises: 3c3f2cfbf10f
Create Date: 2026-09-13 18:53:39.880515

"""
# pylint: disable=invalid-name
from typing import Sequence, Union

from alembic import op  # pylint: disable=no-name-in-module


# revision identifiers, used by Alembic.
revision: str = '123bca2708a4'
down_revision: Union[str, Sequence[str], None] = '3c3f2cfbf10f'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Create black_and_white schema and grant privileges."""
    op.execute("CREATE SCHEMA IF NOT EXISTS black_and_white")

    # Grant usage + create on the schema to a role/user
    op.execute("GRANT ALL PRIVILEGES ON SCHEMA black_and_white TO postgres")

    # Grant privileges on all existing tables/sequences in the schema
    op.execute("GRANT ALL PRIVILEGES ON ALL TABLES IN SCHEMA black_and_white TO postgres")
    op.execute("GRANT ALL PRIVILEGES ON ALL SEQUENCES IN SCHEMA black_and_white TO postgres")

    # Ensure future tables/sequences created in this schema also get the grants
    op.execute(
        "ALTER DEFAULT PRIVILEGES IN SCHEMA black_and_white "
        "GRANT ALL PRIVILEGES ON TABLES TO postgres"
    )
    op.execute(
        "ALTER DEFAULT PRIVILEGES IN SCHEMA black_and_white "
        "GRANT ALL PRIVILEGES ON SEQUENCES TO postgres"
    )


def downgrade() -> None:
    """Drop black_and_white schema."""
    op.execute("DROP SCHEMA IF EXISTS black_and_white CASCADE")
