from wildlife_tracker.migration_tracking.migration_path import MigrationPath
from wildlife_tracker.habitat_management.habitat import Habitat
from typing import Optional

class MigrationPath:

    def __init__(self, 
                 path_id: int,
                 migration_path: MigrationPath,
                 start_location: Habitat,
                 destination: Habitat,
                 duration: Optional[int] = None
                 ) -> None:
        self.path_id = path_id
        self.migration_path = migration_path
        self.start_location = start_location
        self.destination = destination
        self.duration = duration

    def get_migration_path_details(path_id) -> dict:
        pass

    def update_migration_path_details(path_id: int, **kwargs) -> None:
        pass