from app.persistence.repository import InMemoryRepository


class hBnBFacade:
    def __init__(self):
        self.user_repo = InMemoryRepository()
        self.place_repo = InMemoryRepository()
        self.review_repo = InMemoryRepository()
        self.amenity_repo = InMemoryRepository()

    def create_user(self, user_data):
        pass

    def get_user(self, user_id):
        pass

    def get_all_users(self):
        pass

    def update_user(self, user_id):
        pass

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
    def create_review(self):
        pass

    def get_review(self, review_id):
        pass

    def get_all_reviews(self):
        pass

    def update_review(self):
        pass

# <------------------------------------------------------------------------>
    def create_amenity(self):
        pass

    def get_amenity(self, amenity_id):
        pass

    def get_all_amenity(self):
        pass

    def update_amenity(self, amenity_id):
        pass