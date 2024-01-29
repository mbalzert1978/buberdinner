from buberdinner.app.error import Error


class InfrastructureError(Error):
    """Base exception for all infrastructure exceptions."""


class NotFoundError(InfrastructureError):
    """Raised when entity was not found in database."""


class JwtError(Error):
    """Base exception for all JWT related exceptions."""
