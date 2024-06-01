from uk_police_client.clients.crimes_client import CrimesClient
from uk_police_client.clients.forces_client import ForcesClient
from uk_police_client.clients.neighbourhoods_client import NeighbourhoodsClient
from uk_police_client.clients.stop_search_client import StopAndSearchClient


class UKPoliceClient(
    ForcesClient, CrimesClient, NeighbourhoodsClient, StopAndSearchClient
):
    def __init__(self, timeout=10):
        super().__init__(timeout=timeout)
