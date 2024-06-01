import pytest
from datetime import datetime
from uk_police_client.utils import format_date


def test_format_date():
    """
    Test the format_date function.

    Ensure that the function correctly formats both date strings and datetime objects into the "YYYY-MM" format.
    """

    # Test with different valid date strings
    assert format_date("2022-06-15") == "2022-06"
    assert format_date("2022/06/15") == "2022-06"
    assert format_date("06/15/2022") == "2022-06"
    assert format_date("15.06.2022") == "2022-06"
    assert format_date("June 15, 2022") == "2022-06"

    # Test with different datetime objects
    assert format_date(datetime(2022, 6, 15)) == "2022-06"
    assert format_date(datetime(2022, 12, 31)) == "2022-12"
    assert format_date(datetime(2023, 1, 1)) == "2023-01"

    # Test with invalid inputs
    with pytest.raises(ValueError):
        format_date(123)
    with pytest.raises(ValueError):
        format_date(None)
    with pytest.raises(ValueError):
        format_date("invalid_date_format")


if __name__ == "__main__":
    import subprocess

    subprocess.call(["pytest", "--tb=short", str(__file__)])
