from typing import Optional, List
from wildlife_tracker.habitat_management.habitat import Habitat
from wildlife_tracker.animal_management.animal import Animal

class HabitatManager:
    # blank animals dict, get ani by id, register ani, remove ani

    def __init__(self,
                 habitats: dict[int, Habitat] = {} ) -> None:
        self.habitats = habitats
    
    def create_habitat(self, habitat_id: int, geographic_area: str, size: int, environment_type: str) -> Habitat:
        pass

    def remove_habitat(self, habitat_id: int) -> None:
        pass

    def get_habitat_by_id(self, habitat_id: int) -> Habitat:
        pass

    def get_habitats_by_geographic_area(self, geographic_area: str) -> List[Habitat]:
        pass

    def get_habitats_by_size(self, size: int) -> List[Habitat]:
        pass

    def get_habitats_by_type(self, environment_type: str) -> List[Habitat]:
        pass

    def assign_animals_to_habitat(self, animals: List[Animal]) -> None:
        pass

