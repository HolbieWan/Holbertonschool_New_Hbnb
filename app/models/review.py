from base_model import BaseModel
from place import Place
from user import User


class Review(BaseModel):
    def __init__(self, text, rating, place, user):
        super().__init__()
        self.text = text
        self.rating = rating
        self.place = place
        self.user = user

    def is_valid(self):
        try:
            if not isinstance(self.text, str):
                raise TypeError("text must be strings (str).")
            
            if not isinstance(self.rating, int):
                raise TypeError("rating must be an integer (int).")
            
            if self.rating < 1 or self.rating > 5:
                raise ValueError("rating must be between 1 and 5.")
            
            if not isinstance(self.place, Place):
                raise TypeError("place must be an instance of class(Place)")
        
            if not isinstance(self.user, User):
                raise TypeError("place must be an instance of class(User)")

        except TypeError as te:
            print(f"Type error: {str(te)}")
            return False

        except ValueError as ve:
            print(f"Value error: {str(ve)}")
            return False

    def to_dict(self):
        return {
            "review_id" : self.id,
            "text" : self.text,
            "rating" : self.rating,
            "place" : self.place,
            "user" : self.user,
            "created_at" : self.created_at,
            "updated_at" : self.updated_at
        }
