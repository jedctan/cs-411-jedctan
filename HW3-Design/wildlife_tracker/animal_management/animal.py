from typing import Any, Optional

class Animal:
#id, geo area, size, env type, animals list (otp)
#update hab, assign ani to hab, get ani in hab, get hab details
    def __init__(self, 
                 animal_id: int,
                 species: str,
                 health_status: Optional[str] = None,
                 age: Optional[int] = None) -> None:
                 
        self.animal_id = animal_id
        self.species = species
        self.health_status = health_status
        self.age = age
    
    def get_animal_details(self, animal_id) -> dict[str, Any]:
        pass 
        
    
