from pydantic import BaseModel, Field


class Lead(BaseModel):
    name: str = Field(..., examples=["Jane Doe"])
    email: str = Field(..., examples=["jane@example.com"])
    company: str = Field(..., examples=["Acme"])


class Message(BaseModel):
    message: str = Field(..., examples=["am interested in your services."])
