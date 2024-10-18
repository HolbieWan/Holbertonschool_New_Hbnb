from app.persistence.repo_selector import RepoSelector
from app.models.place import Place

class PlaceFacade():

    def __init__(self, selected_repo):
        self.place_repo = selected_repo

    # <------------------------------------------------------------------------>

    def create_place(self, place_data):
        pass
    
    def get_place(self, place_id):
        pass

    def get_all_places(self):
        pass

    def update_place(self, place_id):
        pass