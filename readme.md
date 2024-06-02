**UK Police API Client**

---

**Description:**
The UK Police API Client is a Python package that provides convenient access to various data sets from the UK Police API. It allows users to retrieve information about police forces, crimes, stop and searches, and neighborhood policing, among other data sets. Find it here https://data.police.uk/docs/

---

**Installation:**
To install the UK Police API Client, simply use pip:

```
git clone https://github.com/jonah-ramponi/UK-Police-API-Python-Client.git

pip install -e . 
```

---

**Usage:**
Below is an example of how to use the client to retrieve data:

```python
from uk_police_client import CrimesClient

# Create a client instance
client = CrimesClient()

location = {"lat": 52.629729, "lng": -1.131592}
date = "2022-02"

# Retrieve street-level crimes
crimes = client.get_street_level_crimes(location, date)

# Process the data as needed
for crime in crimes:
    print(crime)
```

Here are the other endpoints: 

```
forces = client.get_forces()
force_details = client.get_force_details(force_id)
senior_officers = client.get_force_senior_officers(force_id)

neighbourhoods = client.get_neighbourhoods_for_force(force_id)
neighbourhood = client.get_specific_neighbourhood(force_id, neighbourhood_id)
boundary = client.get_neighbourhood_boundary(force_id, neighbourhood_id)
team = client.get_neighbourhood_team(force_id, neighbourhood_id)
events = client.get_neighbourhood_events(force_id, neighbourhood_id)
priorities = client.get_neighbourhood_priorities(force_id, neighbourhood_id)
neighbourhood_info = client.locate_neighbourhood(coordinates)

crimes = client.get_street_level_crimes(location, date)
outcomes = client.get_street_level_outcomes(location, date)
crimes = client.get_crimes_at_location(location, date)
crimes = client.get_crimes_no_location(category, force, date)
categories = client.get_crime_categories(date)
last_updated_date = client.get_last_updated_date()
outcomes = client.get_outcomes_for_crime(crime_id)

searches = client.get_stop_and_searches_by_area(location, date)
searches = client.get_stop_and_searches_by_location(location_id, date)
searches = client.get_stops_no_location(force, date)
searches = client.get_stops_by_force(force, date)
```

---

**TODO:**
- Integrating fuzzy matching / force id lookup
- better input handling using pydantic
- make client easier to use (create force object, then access things like .crimes or .location)

---

**Features:**
- Retrieve information about police forces, including their details and senior officers.
- Access crime data at various levels of granularity, such as street-level crimes, outcomes, and crime categories.
- Retrieve stop and search data, including searches by area, location, force, and without location.
- Access neighborhood policing data, including neighborhood details, boundaries, teams, events, and priorities.

---


**Acknowledgments:**
- This project is inspired by the official UK Police API.
- Special thanks to the contributors and maintainers of the UK Police API Client.

---

**Disclaimer:**
This package is not affiliated with or endorsed by the UK Police API. Please refer to the official documentation for terms of use and data usage policies.

--- 