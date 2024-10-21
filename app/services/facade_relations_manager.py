

class FacadeRelationManager:
    def __init__(self, user_facade, place_facade):
        self.user_facade = user_facade
        self.place_facade = place_facade

    def create_place_for_user(self, user_id, place_data):
        user = self.user_facade.user_repo.get(user_id)
       
        if not user:
            raise ValueError(f"User with id {user_id} not found.")

        place_data['owner_id'] = user_id
        place = self.place_facade.create_place(place_data)
        user.places.append(place['id'])
        self.user_facade.user_repo.update(user_id, user.to_dict())

        return place
    
    def get_all_places_from_owner(self, user_id):
        user = self.user_facade.user_repo.get(user_id)

        if not user:
            raise ValueError(f"Usier with id: {user_id} not found")
        
    
        
        