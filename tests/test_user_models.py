import unittest

import pytest
from pydantic import ValidationError

from app.models.user_models import UserMessage


@pytest.mark.unit
class TestUserMessage(unittest.TestCase):
    def test_should_be_valid_when_message_is_within_limits(self):
        """Test if UserMessage is valid with a standard message."""
        data = {"message": "Hello, chatbot!"}
        user_msg = UserMessage(**data)
        self.assertEqual(user_msg.message, data["message"])

    def test_should_raise_error_when_message_is_empty(self):
        """Test if UserMessage raises error when message is empty."""
        data = {"message": ""}
        with self.assertRaises(ValidationError):
            UserMessage(**data)

    def test_should_raise_error_when_message_exceeds_max_length(self):
        """Test if UserMessage raises error when message exceeds 500 characters."""
        data = {"message": "a" * 501}
        with self.assertRaises(ValidationError):
            UserMessage(**data)

    def test_should_raise_error_when_message_field_is_missing(self):
        """Test if UserMessage raises error when message field is missing."""
        data = {}
        with self.assertRaises(ValidationError):
            UserMessage(**data)
