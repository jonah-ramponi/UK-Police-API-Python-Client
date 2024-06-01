"""
    Client for the Forces endpoints
"""

from typing import Dict, Any, List

from uk_police_client.clients.base_client import BaseClient


class ForcesClient(BaseClient):
    """Client for accessing police force data from the UK Police API."""

    def __init__(self, timeout=10):
        super().__init__(timeout=timeout)

    def get_forces(self):
        """
        Retrieves a list of all police forces available via the API.

        The British Transport Police is excluded from the list, as per the API documentation.

        Returns:
            A list of dictionaries containing information about police forces.
            Each dictionary contains 'id' (unique force identifier) and 'name' (force name) keys.
        """

        return self._get("/forces")

    def get_force_details(self, force_id: str) -> Dict[str, Any]:
        """
        Retrieves details of a specific police force.

        Args:
            force_id: The unique identifier of the police force.

        Returns:
            A dictionary containing detailed information about the specified police force.

            Example Return Data (force_id = "leicestershire")

            {
                "description": "A police service for everyone...",
                "url": "http://www.leics.police.uk/",
                "engagement_methods": [
                    {
                        "url": "http://www.facebook.com/pages/Leicester/Leicestershire-Police/76807881169",
                        "description": "Become friends with Leicestershire Constabulary",
                        "title": "Facebook"
                    },
                ],
                "telephone": "0116 222 2222",
                "id": "leicestershire",
                "name": "Leicestershire Constabulary"
            }

        """
        endpoint = f"/forces/{force_id}"
        return self._get(endpoint)

    def get_force_senior_officers(self, force_id: str) -> List[Dict[str, Any]]:
        """
        Retrieves details of senior officers for a specific police force.

        Args:
            force_id: The unique identifier of the police force.

        Returns:
            A list of dictionaries containing detailed information about senior officers of the specified police force.

            Example Return Data (force_id = "leicestershire")

            [
                {
                    "bio": "Roger joined Lincolnshire Police in 1988 ...",
                    "contact_details": {
                        "twitter": "http://www.twitter.com/ACCCLeicsPolice"
                    },
                    "name": "Roger Bannister",
                    "rank": "Assistant Chief Officer (Crime)"
                },
                ...
            ]
        """
        endpoint = f"/forces/{force_id}/people"
        return self._get(endpoint)
