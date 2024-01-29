class InfrastructureError(Exception):
    """Base exception for all infrastructure exceptions."""


class NotFoundError(InfrastructureError):
    """Raised when entity was not found in database."""
