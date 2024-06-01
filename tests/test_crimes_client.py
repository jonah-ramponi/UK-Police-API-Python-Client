from uk_police_client import CrimesClient


def test_get_street_level_crimes():
    """Test case for CrimesClient.get_street_level_crimes method."""
    client = CrimesClient()

    location = {"lat": 52.629729, "lng": -1.131592}
    date = "2022-02"
    crimes = client.get_street_level_crimes(location, date)

    assert isinstance(crimes, list)
    assert all(isinstance(crime, dict) for crime in crimes)
    assert all(
        "category" in crime
        and "location_type" in crime
        and "location" in crime
        and "context" in crime
        and "outcome_status" in crime
        and "persistent_id" in crime
        and "id" in crime
        and "location_subtype" in crime
        and "month" in crime
        for crime in crimes
    )


def test_get_street_level_outcomes():
    """Test case for CrimesClient.get_street_level_outcomes method."""
    client = CrimesClient()

    location = {"lat": 52.629729, "lng": -1.131592}
    date = "2022-02"
    outcomes = client.get_street_level_outcomes(location, date)

    assert isinstance(outcomes, list)
    assert all(isinstance(outcome, dict) for outcome in outcomes)
    assert all(
        "category" in outcome
        and "date" in outcome
        and "person_id" in outcome
        and "crime" in outcome
        for outcome in outcomes
    )


def test_get_crimes_at_location():
    """Test case for CrimesClient.get_crimes_at_location method."""
    client = CrimesClient()

    location = {"lat": 52.629729, "lng": -1.131592}
    date = "2022-02"
    crimes = client.get_crimes_at_location(location, date)

    assert isinstance(crimes, list)
    assert all(isinstance(crime, dict) for crime in crimes)
    assert all(
        "category" in crime
        and "location_type" in crime
        and "location" in crime
        and "context" in crime
        and "outcome_status" in crime
        and "persistent_id" in crime
        and "id" in crime
        and "location_subtype" in crime
        and "month" in crime
        for crime in crimes
    )


def test_get_crimes_no_location():
    """Test case for CrimesClient.get_crimes_no_location method."""
    client = CrimesClient()

    category = "all-crime"
    force = "leicestershire"
    date = "2022-03"
    crimes = client.get_crimes_no_location(category, force, date)

    assert isinstance(crimes, list)
    assert all(isinstance(crime, dict) for crime in crimes)
    assert all(
        "category" in crime
        and "persistent_id" in crime
        and "location_subtype" in crime
        and "id" in crime
        and "location" in crime
        and "context" in crime
        and "month" in crime
        and "location_type" in crime
        and "outcome_status" in crime
        for crime in crimes
    )


def test_get_crime_categories():
    """Test case for CrimesClient.get_crime_categories method."""
    client = CrimesClient()

    date = "2011-08"
    categories = client.get_crime_categories(date)

    assert isinstance(categories, list)
    assert all(isinstance(category, dict) for category in categories)
    assert all("url" in category and "name" in category for category in categories)


def test_get_last_updated_date():
    """Test case for CrimesClient.get_last_updated_date method."""
    client = CrimesClient()

    last_updated_date = client.get_last_updated_date()

    assert isinstance(last_updated_date, dict)
    assert "date" in last_updated_date


def test_get_outcomes_for_crime():
    """Test case for CrimesClient.get_outcomes_for_crime method."""
    client = CrimesClient()

    crime_id = "893e4171b5d2f7ec2c250ad7b970e4a1d1238cd1b567f1a21e07d0110e986381"
    outcomes = client.get_outcomes_for_crime(crime_id)

    assert isinstance(outcomes, dict)
    assert "crime" in outcomes
    assert "outcomes" in outcomes


if __name__ == "__main__":
    import subprocess

    subprocess.call(["pytest", "--tb=short", str(__file__)])
