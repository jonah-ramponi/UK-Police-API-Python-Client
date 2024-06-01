import httpx
from typing import Optional


class BaseClient:
    """Base client for accessing the UK Police API."""

    BASE_URL = "https://data.police.uk/api"

    def __init__(self, timeout=10):
        """
        Initializes the BaseClient with an HTTP client.

        Args:
            timeout: Timeout value for HTTP requests, defaults to 10 seconds.
        """
        self.client = httpx.Client(base_url=self.BASE_URL, timeout=timeout)

    def _get(self, endpoint: str, params: Optional[dict] = None) -> dict:
        """
        Sends a GET request to the specified endpoint.

        Args:
            endpoint: The API endpoint to send the request to.
            params: Optional dictionary of query parameters.

        Returns:
            The response data as a dictionary.
        """
        response = self.client.get(endpoint, params=params)
        response.raise_for_status()
        return response.json()
