"""
    Client for the Crimes endpoints
"""

from typing import Optional, Dict, Any, List

from uk_police_client.clients.base_client import BaseClient


class CrimesClient(BaseClient):
    """Client for accessing crimes data from the UK Police API."""

    def __init__(self, timeout=10):
        super().__init__(timeout=timeout)

    def get_street_level_crimes(
        self, location: dict, date: Optional[str] = None
    ) -> List[Dict[str, Any]]:
        """
        Retrieves street-level crimes data based on a specific location.

        Args:
            location: Dictionary containing the location parameters.
                For a specific point:
                    {'lat': Latitude, 'lng': Longitude}
                For a custom area:
                    {'poly': 'lat1,lng1:lat2,lng2:lat3,lng3', ...}
            date: Optional. Limit results to a specific month in YYYY-MM format.
                  Defaults to the latest month if not provided.

        Returns:
            A list of dictionaries containing street-level crimes data.

            Example Response (location = {"poly" : "52.268,0.543:52.794,0.238:52.130,0.478"}, date= "2022-01")
            [
                {
                    "category": "anti-social-behaviour",
                    "location_type": "Force",
                    "location": {
                        "latitude": "52.640961",
                        "street": {
                            "id": 884343,
                            "name": "On or near Wharf Street North"
                        },
                        "longitude": "-1.126371"
                    },
                    "context": "",
                    "outcome_status": null,
                    "persistent_id": "",
                    "id": 54164419,
                    "location_subtype": "",
                    "month": "2022-01"
                },
                ...
            ]

        """
        params = {"date": date, **location}
        return self._get("/crimes-street/all-crime", params=params)

    def get_street_level_outcomes(
        self, location: dict, date: Optional[str] = None
    ) -> List[Dict[str, Any]]:
        """
        Retrieves street-level outcomes data based on a specific location.

        Args:
            location: Dictionary containing the location parameters.
                For a specific location ID:
                    {'location_id': Location ID}
                For a specific point:
                    {'lat': Latitude, 'lng': Longitude}
                For a custom area:
                    {'poly': 'lat1,lng1:lat2,lng2:lat3,lng3', ...}
            date: Optional. Limit results to a specific month in YYYY-MM format.
                  Defaults to the latest month if not provided.

        Returns:
            A list of dictionaries containing street-level outcomes data.

            Example Response (location = {"poly" : "52.268,0.543:52.794,0.238:52.130,0.478"}, date= "2022-01"):

            [
                {
                    "category": {
                        "code": "unable-to-prosecute",
                        "name": "Unable to prosecute suspect"
                    },
                    "date": "2022-01",
                    "person_id": null,
                    "crime": {
                        "category": "theft-from-the-person",
                        "location_type": "Force",
                        "location": {
                            "latitude": "52.634474",
                            "street": {
                                "id": 883498,
                                "name": "On or near Kate Street"
                            },
                            "longitude": "-1.149197"
                        },
                        "context": "",
                        "persistent_id": "a5a98275facee535b959b236130f5ec05205869fb3d0804c9b14296fcd0bce46",
                        "id": 53566126,
                        "location_subtype": "ROAD",
                        "month": "2016-12"
                    }
                }
            ]
        """
        params = {"date": date, **location}
        return self._get("/outcomes-at-location", params=params)

    def get_crimes_at_location(
        self, location: dict, date: Optional[str] = None
    ) -> List[Dict[str, Any]]:
        """
        Retrieves crimes data at a specific location.

        Args:
            location: Dictionary containing the location parameters.
                For a specific location ID:
                    {'location_id': Location ID}
                For a specific point:
                    {'lat': Latitude, 'lng': Longitude}
            date: Optional. Limit results to a specific month in YYYY-MM format.
                  Defaults to the latest month if not provided.

        Returns:
            A list of dictionaries containing crimes data at the specified location.

            Example Response (location = {"lat": 52.629729, "lng": -1.131592}, date= "2022-02"):

            [
                {
                    "category": "violent-crime",
                    "location_type": "Force",
                    "location": {
                        "latitude": "52.643950",
                        "street": {
                            "id": 884227,
                            "name": "On or near Abbey Gate"
                        },
                        "longitude": "-1.143042"
                    },
                    "context": "",
                    "outcome_status": {
                        "category": "Unable to prosecute suspect",
                        "date": "2022-02"
                    },
                    "persistent_id": "4d83433f3117b3a4d2c80510c69ea188a145bd7e94f3e98924109e70333ff735",
                    "id": 54726925,
                    "location_subtype": "",
                    "month": "2022-02"
                }
            ]
        """
        params = {"date": date, **location}
        return self._get("/crimes-at-location", params=params)

    def get_crimes_no_location(
        self, category: str, force: str, date: Optional[str] = None
    ) -> List[Dict[str, Any]]:
        """
        Retrieves crimes data with no mapped location.

        Args:
            category: The category of the crimes.
            force: Specific police force.
            date: Optional. Limit results to a specific month in YYYY-MM format.
                  Defaults to the latest month if not provided.

        Returns:
            A list of dictionaries containing crimes data with no mapped location.

            Example Response (category="all-crime", force="leicestershire", date="2022-03"):
            [
                {
                    "category": "burglary",
                    "persistent_id": "4ea1d4da29bd8b9e362af35cbabb6157149f62b65d37486dffd185a18e1aaadd",
                    "location_subtype": "",
                    "id": 56862854,
                    "location": null,
                    "context": "",
                    "month": "2022-03",
                    "location_type": null,
                    "outcome_status": {
                        "category": "Investigation complete; no suspect identified",
                        "date": "2022-03"
                    }
                },
                ...
            ]
        """

        params = {"category": category, "force": force, "date": date}
        return self._get("/crimes-no-location", params=params)

    def get_crime_categories(self, date: str) -> List[Dict[str, str]]:
        """
        Retrieves a list of valid crime categories for a given data set date.

        Args:
            date: The date of the data set in YYYY-MM format.

        Returns:
            A list of dictionaries containing valid crime categories.

            Example Response (date="2011-08"):
            [
                {
                    "url": "all-crime",
                    "name": "All crime and ASB"
                },
                {
                    "url": "burglary",
                    "name": "Burglary"
                },
                {
                    "url": "anti-social-behaviour",
                    "name": "Anti-social behaviour"
                },
                ...
            ]
        """
        params = {"date": date}
        return self._get("/crime-categories", params=params)

    def get_last_updated_date(self) -> Dict[str, str]:
        """
        Retrieves the month of the latest crime data update.

        Returns:
            A string representing the month of the latest crime data update in ISO format (YYYY-MM).

            Example Response:

            {
                "date": "2011-09-01"
            }
        """
        return self._get("/crime-last-updated")

    def get_outcomes_for_crime(self, crime_id: str) -> Dict[str, Any]:
        """
        Retrieves the outcomes (case history) for the specified crime.

        Args:
            crime_id: The 64-character identifier of the crime.

        Returns:
            A dictionary containing the crime details and outcomes.

            Example Response:
            {
                "crime": {
                    "category": "violent-crime",
                    "persistent_id": "590d68b69228a9ff95b675bb4af591b38de561aa03129dc09a03ef34f537588c",
                    "location_subtype": "",
                    "location_type": "Force",
                    "location": {
                        "latitude": "52.639814",
                        "street": {
                            "id": 883235,
                            "name": "On or near Sanvey Gate"
                        },
                        "longitude": "-1.139118"
                    },
                    "context": "",
                    "month": "2022-05",
                    "id": 56880258
                },
                "outcomes": [
                    {
                        "category": {
                            "code": "under-investigation",
                            "name": "Under investigation"
                        },
                        "date": "2022-05",
                        "person_id": null
                    },
                    {
                        "category": {
                            "code": "formal-action-not-in-public-interest",
                            "name": "Formal action is not in the public interest"
                        },
                        "date": "2022-06",
                        "person_id": null
                    }
                ]
            }
        """
        endpoint = f"/outcomes-for-crime/{crime_id}"
        return self._get(endpoint)
