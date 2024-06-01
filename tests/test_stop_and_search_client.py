from uk_police_client import StopAndSearchClient


def test_get_stop_and_searches_by_area():
    """Test case for StopAndSearchClient.get_stop_and_searches_by_area method."""
    client = StopAndSearchClient()

    location = {"lat": 52.629729, "lng": -1.131592}
    date = "2022-02"
    searches = client.get_stop_and_searches_by_area(location, date)

    assert isinstance(searches, list)
    assert all(isinstance(search, dict) for search in searches)
    assert all(
        "age_range" in search
        and "outcome" in search
        and "involved_person" in search
        and "self_defined_ethnicity" in search
        and "gender" in search
        and "legislation" in search
        and "outcome_linked_to_object_of_search" in search
        and "datetime" in search
        and "removal_of_more_than_outer_clothing" in search
        and "outcome_object" in search
        and "location" in search
        and "operation" in search
        and "officer_defined_ethnicity" in search
        and "type" in search
        and "operation_name" in search
        and "object_of_search" in search
        for search in searches
    )


def test_get_stop_and_searches_by_location():
    """Test case for StopAndSearchClient.get_stop_and_searches_by_location method."""
    client = StopAndSearchClient()

    location_id = "883407"
    date = "2022-02"
    searches = client.get_stop_and_searches_by_location(location_id, date)

    assert isinstance(searches, list)
    assert all(isinstance(search, dict) for search in searches)
    assert all(
        "age_range" in search
        and "self_defined_ethnicity" in search
        and "outcome_linked_to_object_of_search" in search
        and "datetime" in search
        and "removal_of_more_than_outer_clothing" in search
        and "operation" in search
        and "officer_defined_ethnicity" in search
        and "object_of_search" in search
        and "involved_person" in search
        and "gender" in search
        and "legislation" in search
        and "location" in search
        and "outcome" in search
        and "type" in search
        and "operation_name" in search
        for search in searches
    )


def test_get_stops_no_location():
    """Test case for StopAndSearchClient.get_stops_no_location method."""
    client = StopAndSearchClient()

    force = "leicestershire"
    date = "2022-03"
    searches = client.get_stops_no_location(force, date)

    assert isinstance(searches, list)
    assert all(isinstance(search, dict) for search in searches)
    assert all(
        "age_range" in search
        and "self_defined_ethnicity" in search
        and "outcome_linked_to_object_of_search" in search
        and "datetime" in search
        and "removal_of_more_than_outer_clothing" in search
        and "operation" in search
        and "officer_defined_ethnicity" in search
        and "object_of_search" in search
        and "involved_person" in search
        and "gender" in search
        and "legislation" in search
        and "location" in search
        and "outcome" in search
        and "type" in search
        and "operation_name" in search
        for search in searches
    )


def test_get_stops_by_force():
    """Test case for StopAndSearchClient.get_stops_by_force method."""
    client = StopAndSearchClient()

    force = "leicestershire"
    date = "2022-03"
    searches = client.get_stops_by_force(force, date)

    assert isinstance(searches, list)
    assert all(isinstance(search, dict) for search in searches)
    assert all(
        "age_range" in search
        and "self_defined_ethnicity" in search
        and "outcome_linked_to_object_of_search" in search
        and "datetime" in search
        and "removal_of_more_than_outer_clothing" in search
        and "operation" in search
        and "officer_defined_ethnicity" in search
        and "object_of_search" in search
        and "involved_person" in search
        and "gender" in search
        and "legislation" in search
        and "location" in search
        and "outcome" in search
        and "type" in search
        and "operation_name" in search
        for search in searches
    )


if __name__ == "__main__":
    import subprocess

    subprocess.call(["pytest", "--tb=short", str(__file__)])
