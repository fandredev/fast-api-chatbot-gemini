from pydantic import BaseModel, Field


class UserMessage(BaseModel):
    """Model to represent a message sent by the user."""

    message: str = Field(
        ...,
        min_length=1,
        max_length=500,
        description="The message sent by the user to the chatbot.",
    )
