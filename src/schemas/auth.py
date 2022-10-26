from pydantic import BaseModel
from pydantic.fields import Field


class RefreshTokenRequest(BaseModel):
    refresh_token: str


class AccessToken(BaseModel):
    access_token: str


class TokenResponse(AccessToken, RefreshTokenRequest):
    pass


# ===============================================================================


class AuthBase(BaseModel):
    username: str
    password: str


class LoginRequest(AuthBase):
    pass


class RegistrationRequest(AuthBase):
    password_repeat: str


class User(BaseModel):
    id: int
    username: str
    password: str = Field(None, exclude=True)
