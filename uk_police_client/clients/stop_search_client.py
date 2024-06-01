"""
    Client for the Stop & Search endpoints
"""

from typing import Optional, Dict, Any, List

from uk_police_client.clients.base_client import BaseClient


class StopAndSearchClient(BaseClient):
    """Client for accessing stop and searches data from the UK Police API."""

    def __init__(self, timeout=10):
        super().__init__(timeout=timeout)

    def get_stop_and_searches_by_area(
        self, location: dict, date: Optional[str] = None
    ) -> List[Dict[str, Any]]:
        """
        Retrieves stop and searches data based on a specific area.

        Args:
            location: Dictionary containing the location parameters.
                For a specific point:
                    {'lat': Latitude, 'lng': Longitude}
                For a custom area:
                    {'poly': 'lat1,lng1:lat2,lng2:lat3,lng3', ...}
            date: Optional. Limit results to a specific month in YYYY-MM format.
                  Defaults to the latest month if not provided.

        Returns:
            A list of dictionaries containing stop and searches data.

            Example Response:
            [
                {
                    "age_range": "18-24",
                    "outcome": "Summons \/ charged by post",
                    "involved_person": true,
                    "self_defined_ethnicity": "White - English\/Welsh\/Scottish\/Northern Irish\/British",
                    "gender": "Male",
                    "legislation": "Misuse of Drugs Act 1971 (section 23)",
                    "outcome_linked_to_object_of_search": true,
                    "datetime": "2018-06-06T12:20:00+00:00",
                    "removal_of_more_than_outer_clothing": false,
                    "outcome_object": {
                        "id": "bu-summons",
                        "name": "Summons \/ charged by post"
                    },
                    "location": {
                        "latitude": "52.631569",
                        "street": {
                            "id": 1489803,
                            "name": "Leicester (Station)"
                        },
                        "longitude": "-1.124283"
                    },
                    "operation": null,
                    "officer_defined_ethnicity": "White",
                    "type": "Person search",
                    "operation_name": null,
                    "object_of_search": "Controlled drugs"
                },
                ...
            ]
        """
        params = {"date": date, **location}
        return self._get("/stops-street", params=params)

    def get_stop_and_searches_by_location(
        self, location_id: str, date: Optional[str] = None
    ) -> List[Dict[str, Any]]:
        """
        Retrieves stop and searches data at a specific location.

        Args:
            location_id: The ID of the location to get stop and searches for.
            date: Optional. Limit results to a specific month in YYYY-MM format.
                  Defaults to the latest month if not provided.

        Returns:
            A list of dictionaries containing stop and searches data.

            Example Response:
            [
                {
                    "age_range": "10-17",
                    "self_defined_ethnicity": "White - White British (W1)",
                    "outcome_linked_to_object_of_search": true,
                    "datetime": "2017-01-14T20:50:00+00:00",
                    "removal_of_more_than_outer_clothing": null,
                    "operation": null,
                    "officer_defined_ethnicity": "White",
                    "object_of_search": "Controlled drugs",
                    "involved_person": true,
                    "gender": "Female",
                    "legislation": "Misuse of Drugs Act 1971 (section 23)",
                    "location": {
                        "latitude": "52.634407",
                        "street": {
                            "id": 883407,
                            "name": "On or near Shopping Area"
                        },
                        "longitude": "-1.133653"
                    },
                    "outcome": "Local resolution",
                    "type": "Person search",
                    "operation_name": null
                },
                ...
            ]
        """
        params = {"location_id": location_id, "date": date}
        return self._get("/stops-at-location", params=params)

    def get_stops_no_location(
        self, force: str, date: Optional[str] = None
    ) -> List[Dict[str, Any]]:
        """
        Retrieves stop and searches data that could not be mapped to a location.

        Args:
            force: The force that carried out the stop and searches.
            date: Optional. Limit results to a specific month in YYYY-MM format.
                  Defaults to the latest month if not provided.

        Returns:
            A list of dictionaries containing stop and searches data with no location.

            Example Response:
            [
                {
                    "age_range": "over 34",
                    "self_defined_ethnicity": "White - White British (W1)",
                    "outcome_linked_to_object_of_search": null,
                    "datetime": "2017-01-24T01:50:00+00:00",
                    "removal_of_more_than_outer_clothing": null,
                    "operation": null,
                    "officer_defined_ethnicity": "White",
                    "object_of_search": "Controlled drugs",
                    "involved_person": true,
                    "gender": "Male",
                    "legislation": "Misuse of Drugs Act 1971 (section 23)",
                    "location": null,
                    "outcome": false,
                    "type": "Person search",
                    "operation_name": null
                },
                ...
            ]
        """
        params = {"force": force, "date": date}
        return self._get("/stops-no-location", params=params)

    def get_stops_by_force(
        self, force: str, date: Optional[str] = None
    ) -> List[Dict[str, Any]]:
        """
        Retrieves stop and searches reported by a particular force.

        Args:
            force: The force ID of the force to get stop and searches for.
            date: Optional. Limit results to a specific month in YYYY-MM format.
                  Defaults to the latest month if not provided.

        Returns:
            A list of dictionaries containing stop and searches data reported by the specified force.

            Example Response:
            [
                {
                    "age_range": "18-24",
                    "self_defined_ethnicity": "Mixed - Any other Mixed ethnic background (M9)",
                    "outcome_linked_to_object_of_search": null,
                    "datetime": "2017-01-01T02:24:09+00:00",
                    "removal_of_more_than_outer_clothing": false,
                    "operation": false,
                    "officer_defined_ethnicity": "Other",
                    "object_of_search": "Controlled drugs",
                    "involved_person": true,
                    "gender": "Male",
                    "legislation": "Misuse of Drugs Act 1971 (section 23)",
                    "location": {
                        "latitude": "51.127234",
                        "street": {
                            "id": 532290,
                            "name": "On or near Nightclub"
                        },
                        "longitude": "-3.008284"
                    },
                    "outcome": false,
                    "type": "Person search",
                    "operation_name": null
                },
                ...
            ]
        """
        params = {"force": force, "date": date}
        return self._get("/stops-force", params=params)
