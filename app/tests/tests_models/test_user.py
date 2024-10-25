from datetime import datetime

from app.models.user import User
from app.models.place import Place


def test_user_creation():
    user = User(
        first_name="John",
        last_name="Doe",
        email="john.doe@example.com")
    assert user.first_name == "John"
    assert user.last_name == "Doe"
    assert user.email == "john.doe@example.com"
    assert user.is_admin is False  # Default value
    print("User creation test passed!")


test_user_creation()


def test_is_valid():
    user1 = User(
        first_name="Johnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn",
        last_name="Doe",
        email="john.doe@example.com")
    assert user1.is_valid() == False
    user2 = User(
        first_name="John",
        last_name="Doeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee",
        email="john.doe@example.com")
    assert user2.is_valid() == False
    user3 = User(first_name="John", last_name="Doe", email="john.doe@example")
    assert user3.is_valid() == False
    user4 = User(
        first_name="John",
        last_name="Doe",
        email="john.doe@google.com")
    assert user4.is_valid()
    print("User.isvalid() test passed")


test_is_valid()


def test_add_place():
    user1 = User(first_name="John", last_name="Doe", email="john.doe@example")
    place1 = Place(
        title="Chez John",
        description="Great place",
        price=200,
        latitude=30,
        longitude=100,
        owner_id=user1)

    user1.add_place(place1)

    if place1 in user1.places:
        print(user1)
        print("User.add_place() test passed")
    else:
        raise ValueError("add_place() test failed")


test_add_place()


def test_to_dict():
    user1 = User(
        first_name="John",
        last_name="Doe",
        email="john.doe@example.com",
        is_admin=False,
    )

    user_dict = user1.to_dict()

    expected_dict = {
        "user_id": user1.id,
        "first_name": "John",
        "last_name": "Doe",
        "email": "john.doe@example.com",
        "is_admin": False,
        "places": [],
        "created_at": user1.created_at,
        "updated_at": user1.updated_at
    }

    assert user_dict == expected_dict, f"Expected {expected_dict}, but got {user_dict}"
    print("to_dict() test passed!")


test_to_dict()
