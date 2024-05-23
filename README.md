# dcr-python-exercise

Exercises
Exercise 1 - Add script called add_states.py in src folder to provide aggregated stats for each region.

Exercise 2 - Integrate with API
update this management command <pyhton python load_data.py> to obtain the JSON input data from this url: https://storage.googleapis.com/dcr-django-test/countries.json

Exercise 3 - Store additional Data
update the database tables and management command to also import:
topLevelDomain
capital

SQL Commands used for above db changes are listed here

<sqlite3 .\countries.db>

sqlite> ALTER TABLE country ADD COLUMN topLevelDomain TEXT;

sqlite> ALTER TABLE country ADD COLUMN capital TEXT;

sqlite> PRAGMA table_info(country);
0|id|INTEGER|0||1
1|name|TEXT|0||0
2|alpha2Code|TEXT|0||0
3|alpha3Code|TEXT|0||0
4|population|INTEGER|0||0
5|region_id|INTEGER|0||0
6|topLevelDomain|TEXT|0||0
7|capital|TEXT|0||0
