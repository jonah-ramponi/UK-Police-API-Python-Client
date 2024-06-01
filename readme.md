**UK Police API Client**

---

**Description:**
The UK Police API Client is a Python package that provides convenient access to various data sets from the UK Police API. It allows users to retrieve information about police forces, crimes, stop and searches, and neighborhood policing, among other data sets. Find it here https://data.police.uk/docs/

---

**Installation:**
To install the UK Police API Client, simply use pip:

```
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