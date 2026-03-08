from fastapi import Request
from fastapi.responses import JSONResponse
from app.core.exceptions import (
    EmailAlreadyExistsException,
    UsernameAlreadyExistsException,
    InvalidCredentialsException,
    InvalidTokenException
)

def register_exception_handlers(app):
    
    @app.exception_handler(EmailAlreadyExistsException)
    def email_exists_handler(request: Request, exc: EmailAlreadyExistsException):
        return JSONResponse(status_code=409, content={"detail": str(exc)})

    @app.exception_handler(UsernameAlreadyExistsException)
    def username_exists_handler(request: Request, exc: UsernameAlreadyExistsException):
        return JSONResponse(status_code=409, content={"detail": str(exc)})

    @app.exception_handler(InvalidCredentialsException)
    def invalid_credentials_handler(request: Request, exc: InvalidCredentialsException):
        return JSONResponse(status_code=401, content={"detail": str(exc)})

    @app.exception_handler(InvalidTokenException)
    def invalid_token_handler(request: Request, exc: InvalidTokenException):
        return JSONResponse(status_code=401, content={"detail": str(exc)})