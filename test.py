from uk_police_client import CrimesClient

client = CrimesClient()

location = {"lat": 52.629729, "lng": -1.131592}
date = "2022-02"
crimes = client.get_street_level_crimes(location, date)
print(crimes)
