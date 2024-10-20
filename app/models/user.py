from app.models.base_model import BaseModel
from email_validator import validate_email, EmailNotValidError


class User(BaseModel):
    def __init__(self, first_name, last_name, email, is_admin=False):
        super().__init__()
        self.type = type
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.is_admin = is_admin
        self.places = []

    def add_place(self, place):
        self.places.append(place)    
    
    def is_valid(self):
        try:
            if not all(isinstance(attr, str) for attr in [self.email, self.first_name, self.last_name]):
                print("Validation failed: First name, last name, or email is not a string.")
                raise TypeError("email, first_name, and last_name must be strings (str).")

            if len(self.first_name) > 50 or len(self.last_name) > 50:
                print("Validation failed: First name or last name exceeds 50 characters.")
                raise ValueError("first_name and last_name must be less than 50 characters.")

            valid = validate_email(self.email)
            return True

        except TypeError as te:
            print(f"Type error: {str(te)}")
            return False
        
        except EmailNotValidError as e:
            print(f"Email validation failed: {str(e)}")
            return False

        except ValueError as ve:
            print(f"Value error: {str(ve)}")
            return False

    def to_dict(self):
        return {
            "type": "user",
            "id" : self.id,
            "first_name" : self.first_name,
            "last_name" : self.last_name,
            "email" : self.email,
            "is_admin" : self.is_admin,
            "places" : self.places,
            "created_at" : self.created_at.isoformat(),
            "updated_at" : self.updated_at.isoformat()
        }
