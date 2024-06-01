from uk_police_client import ForcesClient


def test_get_forces():
    """Test case for ForcesClient.get_forces method."""

    client = ForcesClient()

    forces = client.get_forces()

    assert isinstance(forces, list)
    assert all(isinstance(force, dict) for force in forces)
    assert all("id" in force and "name" in force for force in forces)


def test_get_force_details():
    """Test case for ForcesClient.get_force_details method."""

    client = ForcesClient()

    force_id = "leicestershire"
    force_details = client.get_force_details(force_id)

    assert isinstance(force_details, dict)
    assert all(
        key in force_details
        for key in [
            "description",
            "url",
            "engagement_methods",
            "telephone",
            "id",
            "name",
        ]
    )


def test_get_force_senior_officers():
    """Test case for ForcesClient.get_force_senior_officers method."""

    client = ForcesClient()

    force_id = "leicestershire"
    senior_officers = client.get_force_senior_officers(force_id)

    assert isinstance(senior_officers, list)
    assert all(isinstance(officer, dict) for officer in senior_officers)
    assert all("name" in officer and "rank" in officer for officer in senior_officers)


if __name__ == "__main__":
    import subprocess

    subprocess.call(["pytest", "--tb=short", str(__file__)])
