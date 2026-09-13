"""Custom application exception types."""


class AppException(Exception):
    """Base exception for application-level errors with HTTP status and code."""

    def __init__(
        self,
        message: str,
        status_code: int = 400,
        code: str = "APP_ERROR",
    ):
        super().__init__(message)
        self.message = message
        self.status_code = status_code
        self.code = code
