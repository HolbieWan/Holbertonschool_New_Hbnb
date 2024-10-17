from base_model import BaseModel


class Place(BaseModel):
    def __init__(self, title, description, price, latitude, longitude, owner):
        super().__init__()
        self.title = title
        self.description = description
        self.price = price
        self.latitude = latitude
        self.longitude = longitude
        self.owner = owner
        self.reviews = []
        self.amenities = []

    def add_review(self, review):
        """Add a review to the place."""
        self.reviews.append(review)

    def add_amenity(self, amenity):
        """Add an amenity to a place."""
        self.amenities.append(amenity)

    def is_valid(self):
        try:
            if not all(isinstance(attr, str) for attr in [self.title, self.description]):
                raise TypeError("email, first_name, and last_name must be strings (str).")
            
            if self.price < 0:
                raise ValueError("price must be a positiv value")
            
            if len(self.title) > 100:
                raise ValueError("title must be less than 100 characters.")
            
            if not all(isinstance(attr, float) for attr in [self.price, self.latitude, self.longitude]):
                raise TypeError("email, first_name, and last_name must be strings (str).")

            if self.latitude > 90 or self.latitude < -90:
                raise ValueError("Must be within the range of -90.0 to 90.0")
            
            if self.longitude > 180 or self.latitude < -180:
                raise ValueError("Must be within the range of -90.0 to 90.0")

        except TypeError as te:
            print(f"Type error: {str(te)}")
            return False

        except ValueError as ve:
            print(f"Value error: {str(ve)}")
            return False

    def to_dict(self):
        return {
            "place_id" : self.id,
            "title" : self.title,
            "description" : self.description,
            "price" : self.price,
            "latitude" : self.latitude,
            "longitude" : self.longitude,
            "owner" : self.owner,
            "reviews" : self.reviews,
            "amenities" : self.amenities,
            "created_at" : self.created_at,
            "updated_at" : self.updated_at
        }
