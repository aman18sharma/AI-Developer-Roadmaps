"""Logging configuration for the application."""

import logging
import sys


def configure_logging() -> None:
    """Configure root logger to write structured records to stdout."""
    logging.basicConfig(
        level=logging.INFO,
        format=(
            "%(asctime)s "
            "%(levelname)s "
            "%(name)s "
            "%(message)s"
        ),
        handlers=[
            logging.StreamHandler(sys.stdout)
        ],
    )
