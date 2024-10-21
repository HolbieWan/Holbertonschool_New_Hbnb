

class FacadeRelationManager:
    def __init__(self, user_facade, place_facade):
        self.user_facade = user_facade
        self.place_facade = place_facade

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



# #  Place - Amenity relations
# # <------------------------------------------------------------------------>

#     def create_amenity_for_place(self, place_id, amenity_data):
#         user = self.user_facade.user_repo.get(user_id)
       
#         if not user:
#             raise ValueError(f"User with id {user_id} not found.")

#         place_data['owner_id'] = user_id
#         place = self.place_facade.create_place(place_data)
#         user.places.append(place['id'])
#         self.user_facade.user_repo.update(user_id, user.to_dict())

#         return place
    
#         # <------------------------------------------>

#     def get_all_amenities_from_place(self, place_id):
#         user = self.user_facade.user_repo.get(user_id)

#         if not user:
#             raise ValueError(f"Usier with id: {user_id} not found")
        
#         # <------------------------------------------>

#     def update_amenity_from_place(self, amenity_id, place_id):
#         pass

#         # <------------------------------------------>

#     def delete_amenity_from_place(self, amenity_id, place_id):
#         pass

# #  Place - review relations
# # <------------------------------------------------------------------------>

#     def create_reiew_for_place(self, place_id, review_data):
#         user = self.user_facade.user_repo.get(user_id)
       
#         if not user:
#             raise ValueError(f"User with id {user_id} not found.")

#         place_data['owner_id'] = user_id
#         place = self.place_facade.create_place(place_data)
#         user.places.append(place['id'])
#         self.user_facade.user_repo.update(user_id, user.to_dict())

#         return place
    
#         # <------------------------------------------>

#     def get_all_reviews_from_place(self, place_id):
#         user = self.user_facade.user_repo.get(user_id)

#         if not user:
#             raise ValueError(f"Usier with id: {user_id} not found")
        
#         # <------------------------------------------>

#     def update_review_from_place(self, review_id, place_id):
#         pass

#         # <------------------------------------------>

#     def delete_riview_from_place(self, review_id, place_id):
#         pass