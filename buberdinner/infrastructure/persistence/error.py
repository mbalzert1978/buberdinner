from buberdinner.app.shared.error.error import Error


class InfrastructureError(Error):
    """Base exception for all infrastructure exceptions."""


class WriteError(InfrastructureError):
    """Raised when entity could not be written to database."""


class NotFoundError(InfrastructureError):
    """Raised when entity was not found in database."""
