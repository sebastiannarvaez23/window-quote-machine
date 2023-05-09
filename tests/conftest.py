import pytest

from tests.fatories.users import UserFactory
from django.contrib.auth.models import User

@pytest.fixture
def user_creation():
    return UserFactory()