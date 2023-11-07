import typing

from .authentication_result import AuthenticationResult


class AuthenticationInterface(typing.Protocol):
    def login(self, email:str, password:str) -> AuthenticationResult:
        """Log in to the system."""
    
    def register(self, first_name:str, last_name:str, email:str, password:str) -> AuthenticationResult:
        """Register with the system."""