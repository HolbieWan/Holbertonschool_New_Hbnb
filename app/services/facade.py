from app.persistence.repository import InMemoryRepository
from app.models.user import User


class HBnBFacade:
    def __init__(self):
        self.user_repo = InMemoryRepository()
        self.place_repo = InMemoryRepository()
        self.review_repo = InMemoryRepository()
        self.amenity_repo = InMemoryRepository()

#   <------------------------------------------------------------------------>
#   <------------------------------------------------------------------------>

    def create_user(self, user_data):
        print(f"Creating user with data: {user_data}")

        user = User(
            first_name=user_data["first_name"], 
            last_name=user_data["last_name"],
            email=user_data["email"],
            is_admin=user_data["is_admin"]
        )

        existing_user = self.user_repo.get_by_attribute("email", user.email)
        if existing_user:
            print(f"User {user.first_name} {user.last_name} already exists.")
            return None

        if user.is_valid():
            print(f"User {user.first_name} {user.last_name} passed validation.")
            self.user_repo.add(user)  
            return user.to_dict()
        else:
            print(f"User {user.first_name} {user.last_name} failed validation.")
            raise ValueError("Invalid user data.")
        
#   <------------------------------------------------------------------------>

    def get_user(self, user_id):
        user = self.user_repo.get(user_id)
        if user:
            return user.to_dict()
        else:
            raise ValueError(f"User with id {user_id} not found.")
        
#   <------------------------------------------------------------------------>

    def get_user_by_attribute(self, attr):
        pass

#   <------------------------------------------------------------------------>

    def get_all_users(self):
        users = self.user_repo.get_all()
        return [user.to_dict() for user in users]
    
#   <------------------------------------------------------------------------>

    def update_user(self, user_id, new_data):
        user = self.user_repo.get(user_id)
        if user:
            user.update(new_data)
            self.user_repo.update(user_id, new_data)
            return user.to_dict()
        else:
            raise ValueError(f"User with id {user_id} not found.")
        
# <------------------------------------------------------------------------>
# <------------------------------------------------------------------------>
    def create_place(self, place_data):
        pass
    
    def get_place(self, place_id):
        pass

    def get_all_places(self):
        pass

    def update_place(self, place_id):
        pass

# <------------------------------------------------------------------------>
# <------------------------------------------------------------------------>
    def create_review(self):
        pass

    def get_review(self, review_id):
        pass

    def get_all_reviews(self):
        pass

    def update_review(self):
        pass

# <------------------------------------------------------------------------>
# <------------------------------------------------------------------------>
    def create_amenity(self):
        pass

    def get_amenity(self, amenity_id):
        pass

    def get_all_amenity(self):
        pass

    def update_amenity(self, amenity_id):
        pass