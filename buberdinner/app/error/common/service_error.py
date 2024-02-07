from buberdinner.app.error import Error


class ServiceError(Error):
    """Exception raised when an service error occurs."""


class UnreachableError(ServiceError):
    """Exception raised when an unreachable code error occurs."""
