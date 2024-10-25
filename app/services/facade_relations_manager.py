from app.models.amenity import Amenity

class FacadeRelationManager:
    def __init__(self, user_facade, place_facade, amenity_facade, review_facade):
        self.user_facade = user_facade
        self.place_facade = place_facade
        self.amenity_facade = amenity_facade
        self.review_facade = review_facade

# User - place relations
# <------------------------------------------------------------------------>

    def create_place_for_user(self, user_id, place_data):
        user = self.user_facade.user_repo.get(user_id)
       
        if not user:
            raise ValueError(f"User with id {user_id} not found.")

        place_data['owner_id'] = user_id
        place = self.place_facade.create_place(place_data)
        user.places.append(place['id'])
        self.user_facade.user_repo.update(user_id, user.to_dict())

        return place
    
        # <------------------------------------------>

    def get_all_places_from_user_id(self, user_id):
        user = self.user_facade.user_repo.get(user_id)

        if not user:
            raise ValueError(f"Usier with id: {user_id} not found")
        
        places = user.places
       
        return places
        
        # <------------------------------------------>

    def delete_place_from_owner_place_list(self, place_id, user_id):
        user = self.user_facade.user_repo.get(user_id)

        if not user:
            raise ValueError(f"User with id: {user_id} not found")
        
        places = user.places
        if place_id in places:
            places.remove(place_id)
            self.user_facade.user_repo.update(user_id, user.to_dict())
        else:
            print(f"Place ID {place_id} not found in user's places list.")

        self.place_facade.place_repo.delete(place_id)



 #  Place - Amenity relations
 # <------------------------------------------------------------------------>

    def add_amenity_to_a_place(self, place_id, amenity_data):
        place = self.place_facade.place_repo.get(place_id)

        if not place:
            raise ValueError(f"Place: {place_id} not found.")

        if not amenity_data["name"] in place.amenities:
            place.amenities.append(amenity_data['name'])
            self.place_facade.place_repo.update(place_id, place.to_dict())

        amenity = self.amenity_facade.create_amenity(amenity_data)

        return amenity

        # <------------------------------------------>

    def get_all_amenities_id_from_place(self, place_id):
        place = self.place_facade.place_repo.get(place_id)

        if not place:
            raise ValueError(f"Place: {place_id} not found")
        
        amenities = place.amenities

        return amenities

        # <------------------------------------------>

    def get_list_amenities_names_from_place(self, place_id):
        place = self.place_facade.place_repo.get(place_id)

        if not place:
            raise ValueError(f"Place: {place_id} not found")
        
        amenities = place.amenities

        return amenities

        # <------------------------------------------>

    def delete_amenity_from_place_list(self, amenity_name, place_id):
        place = self.place_facade.place_repo.get(place_id)

        if not place:
            raise ValueError(f"Place with id: {place_id} not found")
        
        amenities = place.amenities

        if amenity_name in amenities:
            amenities.remove(amenity_name)
            self.place_facade.place_repo.update(place_id, place.to_dict())
        else:
            print(f"Amenity {amenity_name} not found in places amenities list.")

        self.amenity_facade.amenity_repo.delete(amenity_name)

# #  Place - review relations
# # <------------------------------------------------------------------------>

    def create_review_for_place(self, place_id, review_data):
        place = self.place_facade.place_repo.get(place_id)
    
        if not place:
            raise ValueError(f"User with id {place_id} not found.")

        review = self.review_facade.create_review(review_data)
        place.reviews.append(review['id'])
        self.place_facade.place_repo.update(place_id, place.to_dict())

        return review
    
#         # <------------------------------------------>

    def get_all_reviews_id_from_place(self, place_id):
        place = self.place_facade.place_repo.get(place_id)

        if not place:
            raise ValueError(f"Usier with id: {place_id} not found")
        
        reviews = place.reviews

        return reviews
    
#         # <------------------------------------------>

    def delete_review_from_place_list(self, review_id, place_id):
        place = self.place_facade.place_repo.get(place_id)

        if not place:
            raise ValueError(f"Place with id: {place_id} not found")
        
        reviews = place.reviews

        if review_id in reviews:
            reviews.remove(review_id)
            self.place_facade.place_repo.update(place_id, place.to_dict())
        else:
            print(f"Review {review_id} not found in places reviews list.")

        self.review_facade.review_repo.delete(review_id)