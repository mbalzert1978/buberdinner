class AuthenticationError(Exception):
    """Exception raised when an authentication service error occurs"""


class UserError(AuthenticationError):
    """Exception raised when an user error occurs"""


class PasswordError(AuthenticationError):
    """Exception raised when an password error occurs"""
