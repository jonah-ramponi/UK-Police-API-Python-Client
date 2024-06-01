from uk_police_client.clients.crimes_client import CrimesClient
from uk_police_client.clients.forces_client import ForcesClient
from uk_police_client.clients.neighbourhoods_client import NeighbourhoodsClient
from uk_police_client.clients.stop_search_client import StopAndSearchClient


class UKPoliceClient:
    BASE_URL = "https://data.police.uk/api"

    def __init__(self, timeout=10):
        self.forces = ForcesClient(timeout)
        self.crimes = CrimesClient(timeout)
        self.neighbourhoods = NeighbourhoodsClient(timeout)
        self.stop_and_search = StopAndSearchClient(timeout)
