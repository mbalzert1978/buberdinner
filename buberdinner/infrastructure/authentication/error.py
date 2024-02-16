from buberdinner.app.shared.error.error import Error


class AuthenticationError(Error):
    """Base exception for all authentication related exceptions."""


class JwtError(AuthenticationError):
    """Base exception for all JWT related exceptions."""
