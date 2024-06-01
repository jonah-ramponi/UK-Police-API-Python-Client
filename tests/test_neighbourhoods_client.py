from uk_police_client import NeighbourhoodsClient


def test_get_neighbourhoods_for_force():
    """Test case for NeighbourhoodsClient.get_neighbourhoods_for_force method."""
    client = NeighbourhoodsClient()

    force_id = "leicestershire"
    neighbourhoods = client.get_neighbourhoods_for_force(force_id)

    assert isinstance(neighbourhoods, list)
    assert all(isinstance(neighbourhood, dict) for neighbourhood in neighbourhoods)
    assert all(
        "id" in neighbourhood and "name" in neighbourhood
        for neighbourhood in neighbourhoods
    )


def test_get_specific_neighbourhood():
    """Test case for NeighbourhoodsClient.get_specific_neighbourhood method."""
    client = NeighbourhoodsClient()

    force_id = "leicestershire"
    neighbourhood_id = "NC04"
    neighbourhood = client.get_specific_neighbourhood(force_id, neighbourhood_id)

    assert isinstance(neighbourhood, dict)
    assert "url_force" in neighbourhood
    assert "contact_details" in neighbourhood
    assert "name" in neighbourhood
    assert "links" in neighbourhood
    assert "centre" in neighbourhood
    assert "locations" in neighbourhood
    assert "description" in neighbourhood
    assert "id" in neighbourhood
    assert "population" in neighbourhood


def test_get_neighbourhood_boundary():
    """Test case for NeighbourhoodsClient.get_neighbourhood_boundary method."""
    client = NeighbourhoodsClient()

    force_id = "leicestershire"
    neighbourhood_id = "NC04"
    boundary = client.get_neighbourhood_boundary(force_id, neighbourhood_id)

    assert isinstance(boundary, list)
    assert all(isinstance(coord, dict) for coord in boundary)
    assert all("latitude" in coord and "longitude" in coord for coord in boundary)


def test_get_neighbourhood_team():
    """Test case for NeighbourhoodsClient.get_neighbourhood_team method."""
    client = NeighbourhoodsClient()

    force_id = "leicestershire"
    neighbourhood_id = "NC04"
    team = client.get_neighbourhood_team(force_id, neighbourhood_id)

    assert isinstance(team, list)
    assert all(isinstance(member, dict) for member in team)
    assert all(
        "bio" in member
        and "contact_details" in member
        and "name" in member
        and "rank" in member
        for member in team
    )


def test_get_neighbourhood_events():
    """Test case for NeighbourhoodsClient.get_neighbourhood_events method."""
    client = NeighbourhoodsClient()

    force_id = "leicestershire"
    neighbourhood_id = "NC04"
    events = client.get_neighbourhood_events(force_id, neighbourhood_id)

    assert isinstance(events, list)
    assert all(isinstance(event, dict) for event in events)
    assert all(
        "contact_details" in event
        and "description" in event
        and "title" in event
        and "address" in event
        and "type" in event
        and "start_date" in event
        and "end_date" in event
        for event in events
    )


def test_get_neighbourhood_priorities():
    """Test case for NeighbourhoodsClient.get_neighbourhood_priorities method."""
    client = NeighbourhoodsClient()

    force_id = "leicestershire"
    neighbourhood_id = "NC04"
    priorities = client.get_neighbourhood_priorities(force_id, neighbourhood_id)

    assert isinstance(priorities, list)
    assert all(isinstance(priority, dict) for priority in priorities)
    assert all(
        "action" in priority
        and "issue-date" in priority
        and "action-date" in priority
        and "issue" in priority
        for priority in priorities
    )


def test_locate_neighbourhood():
    """Test case for NeighbourhoodsClient.locate_neighbourhood method."""
    client = NeighbourhoodsClient()

    coordinates = "51.500617,-0.124629"
    neighbourhood_info = client.locate_neighbourhood(coordinates)

    assert isinstance(neighbourhood_info, dict)
    assert "force" in neighbourhood_info
    assert "neighbourhood" in neighbourhood_info


if __name__ == "__main__":
    import subprocess

    subprocess.call(["pytest", "--tb=short", str(__file__)])
