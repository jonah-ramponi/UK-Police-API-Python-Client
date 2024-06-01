"""
    Client for the Neighbourhoods endpoints
"""

from typing import Dict, Any, List

from uk_police_client.clients.base_client import BaseClient


class NeighbourhoodsClient(BaseClient):
    """Client for accessing Neighbourhoods data from the UK Police API."""

    def __init__(self, timeout=10):
        super().__init__(timeout=timeout)

    def get_neighbourhoods_for_force(self, force_id: str) -> List[Dict[str, str]]:
        """
        Retrieves a list of neighbourhoods for a specific police force.

        Args:
            force_id: The unique identifier of the police force.

        Returns:
            A list of dictionaries containing information about neighbourhoods for the specified police force.

            Example Response:
            [
                {
                    "id": "NC04",
                    "name": "City Centre"
                },
                {
                    "id": "NC66",
                    "name": "Cultural Quarter"
                },
                ...
            ]
        """
        endpoint = f"/{force_id}/neighbourhoods"
        return self._get(endpoint)

    def get_specific_neighbourhood(
        self, force_id: str, neighbourhood_id: str
    ) -> Dict[str, Any]:
        """
        Retrieves details of a specific neighbourhood within a police force.

        Args:
            force_id: The unique identifier of the police force.
            neighbourhood_id: The unique identifier of the neighbourhood.

        Returns:
            A dictionary containing detailed information about the specified neighbourhood.

            Example Response:
            {
                "url_force": "http://www.leics.police.uk/local-policing/city-centre",
                "contact_details": {
                    "twitter": "http://www.twitter.com/centralleicsNPA",
                    "facebook": "http://www.facebook.com/leicspolice",
                    "telephone": "101",
                    "email": "centralleicester.npa@leicestershire.pnn.police.uk"
                },
                "name": "City Centre",
                "links": [
                    {
                        "url": "http://www.leicester.gov.uk/",
                        "description": null,
                        "title": "Leicester City Council"
                    }
                ],
                "centre": {
                    "latitude": "52.6389",
                    "longitude": "-1.13619"
                },
                "locations": [
                    {
                        "name": "Mansfield House",
                        "longitude": null,
                        "postcode": "LE1 3GG",
                        "address": "74 Belgrave Gate, Leicester",
                        "latitude": null,
                        "type": "station",
                        "description": null
                    }
                ],
                "description": " (...) ",
                "id": "NC04",
                "population": "0"
            }
        """
        endpoint = f"/{force_id}/{neighbourhood_id}"
        return self._get(endpoint)

    def get_neighbourhood_boundary(
        self, force_id: str, neighbourhood_id: str
    ) -> List[Dict[str, str]]:
        """
        Retrieves the boundary of a specific neighbourhood within a police force.

        Args:
            force_id: The unique identifier of the police force.
            neighbourhood_id: The unique identifier of the neighbourhood.

        Returns:
            A list of dictionaries containing latitude and longitude pairs that make up the boundary of the neighbourhood.

            Example Response:
            [
                {
                    "latitude": "52.6394052587",
                    "longitude": "-1.1458618876"
                },
                {
                    "latitude": "52.6389452755",
                    "longitude": "-1.1457057759"
                },
                ...
                {
                    "latitude": "52.6383706746",
                    "longitude": "-1.1455755443"
                }
            ]
        """
        endpoint = f"/{force_id}/{neighbourhood_id}/boundary"
        return self._get(endpoint)

    def get_neighbourhood_team(
        self, force_id: str, neighbourhood_id: str
    ) -> List[Dict[str, Any]]:
        """
        Retrieves the neighbourhood team for a specific neighbourhood within a police force.

        Args:
            force_id: The unique identifier of the police force.
            neighbourhood_id: The unique identifier of the neighbourhood.

        Returns:
            A list of dictionaries containing information about the members of the neighbourhood team.

            Example Response:
            [
                {
                    "bio": "<p>I joined Leicestershire Police in 1997 and have enjoyed a variety of roles across the County.<br />\n</p>\n<p>I have worked as a Sergeant in the City Centre for the last 6 years in Response and Neighbourhood Policing roles.</p>\n<p>I am now Deputy NPA Commander and am privileged to work with a great team of committed and enthusiastic people.</p>\n<p>We always try and listen to concerns then support and protect the City communities with a problem solving approach.  Please don?t hesitate to contact us with any issues or problems you may have.</p>",
                    "contact_details": {},
                    "name": "Andy Cooper",
                    "rank": "Sgt"
                },
                ...
            ]
        """
        endpoint = f"/{force_id}/{neighbourhood_id}/people"
        return self._get(endpoint)

    def get_neighbourhood_events(
        self, force_id: str, neighbourhood_id: str
    ) -> List[Dict[str, Any]]:
        """
        Retrieves upcoming events for a specific neighbourhood within a police force.

        Args:
            force_id: The unique identifier of the police force.
            neighbourhood_id: The unique identifier of the neighbourhood.

        Returns:
            A list of dictionaries containing information about upcoming events in the neighbourhood.

            Example Response:
            [
                {
                    "contact_details": {},
                    "description": null,
                    "title": "Drop In Beat Surgery",
                    "address": "Nagarjuna Buddhist Centre, 17 Guildhall Lane",
                    "type": "meeting",
                    "start_date": "2016-09-17T12:00:00",
                    "end_date": "2016-09-17T14:00:00"
                },
                ...
            ]
        """
        endpoint = f"/{force_id}/{neighbourhood_id}/events"
        return self._get(endpoint)

    def get_neighbourhood_priorities(
        self, force_id: str, neighbourhood_id: str
    ) -> List[Dict[str, Any]]:
        """
        Retrieves priorities for a specific neighbourhood within a police force.

        Args:
            force_id: The unique identifier of the police force.
            neighbourhood_id: The unique identifier of the neighbourhood.

        Returns:
            A list of dictionaries containing information about the priorities in the neighbourhood.

            Example Response:
            [
                {
                    "action": null,
                    "issue-date": "2016-04-14T00:00:00",
                    "action-date": null,
                    "issue": "<p>To reduce the amount of Anti-Social Behaviour Humberstone Gate, Leicester.</p>"
                },
                {
                    "action": " (...) ",
                    "issue-date": "2015-10-08T00:00:00",
                    "action-date": "2015-12-22T00:00:00",
                    "issue": "<p>To reduce street drinking and drug use in and around Museum Square, Leicester.</p>"
                },
                ...
            ]
        """
        endpoint = f"/{force_id}/{neighbourhood_id}/priorities"
        return self._get(endpoint)

    def locate_neighbourhood(self, coordinates: str) -> Dict[str, str]:
        """
        Locates the neighbourhood policing team responsible for a particular area.

        Args:
            coordinates: Latitude and Longitude separated by a comma, e.g., "51.500617,-0.124629".

        Returns:
            A dictionary containing the police force and neighbourhood identifiers.

            Example Response:
            {
                "force": "metropolitan",
                "neighbourhood": "00BKX6"
            }
        """
        params = {"q": coordinates}
        return self._get("/locate-neighbourhood", params=params)
