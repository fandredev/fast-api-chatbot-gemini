from pydantic import BaseModel, Field


class UserMessage(BaseModel):
    """
    Modelo para representar uma mensagem enviada pelo usuário.
    """

    message: str = Field(
        ...,
        min_length=1,
        max_length=500,
        description="A mensagem enviada pelo usuário para o chatbot.",
    )
