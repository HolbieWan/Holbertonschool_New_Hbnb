from app.persistence.repo_selector import RepoSelector
from app.models.review import Review

class ReviewFacade():

    def __init__(self, selected_repo):
        self.review_repo = selected_repo

    # <------------------------------------------------------------------------>

    def create_review(self):
        pass

    def get_review(self, review_id):
        pass

    def get_all_reviews(self):
        pass

    def update_review(self):
        pass