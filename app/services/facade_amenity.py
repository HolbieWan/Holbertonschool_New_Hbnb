from app.persistence.repo_selector import RepoSelector
from app.models.amenity import Amenity

class AmenityFacade():

    def __init__(self, selected_repo):
        self.amenity_repo = selected_repo

    # <------------------------------------------------------------------------>

    def create_amenity(self):
        pass

    def get_amenity(self, amenity_id):
        pass

    def get_all_amenity(self):
        pass

    def update_amenity(self, amenity_id):
        pass