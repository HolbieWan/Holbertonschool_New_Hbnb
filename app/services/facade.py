from app.services.facade_user import UserFacade
from app.services.facade_place import PlaceFacade
from app.services.facade_review import ReviewFacade
from app.services.facade_amenity import AmenityFacade
from app.persistence.repo_selector import RepoSelector


class HBnBFacade:
    def __init__(self, repo_type="in_memory"):
        
        user_repo_selector = RepoSelector(repo_type, "user_data.json") 
        place_repo_selector = RepoSelector(repo_type, "place_data.json") 
        review_repo_selector = RepoSelector(repo_type, "review_data.json")  
        amenity_repo_selector = RepoSelector(repo_type, "amenity_data.json")

        user_repo = user_repo_selector.select_repo()
        place_repo = place_repo_selector.select_repo()
        review_repo = review_repo_selector.select_repo()
        amenity_repo = amenity_repo_selector.select_repo()

        self.user_facade = UserFacade(user_repo)
        self.place_facade = PlaceFacade(place_repo)
        self.review_facade = ReviewFacade(review_repo)
        self.amenity_facade = AmenityFacade(amenity_repo)
