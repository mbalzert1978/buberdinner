from buberdinner.app.shared.error import Error


class AuthenticationError(Error):
    """Exception raised when an authentication service error occurs"""


class UserError(AuthenticationError):
    """Exception raised when an user error occurs"""


class PasswordError(AuthenticationError):
    """Exception raised when an password error occurs"""
