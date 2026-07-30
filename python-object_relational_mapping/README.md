# python-object_relational_mapping

This project links Python to MySQL, first using the raw MySQLdb module to
write and execute SQL queries directly, then using SQLAlchemy as an Object
Relational Mapper (ORM) to interact with the database purely through Python
objects, without writing any SQL.

## Learning Objectives

- How to connect to a MySQL database from a Python script
- How to SELECT rows in a MySQL table from a Python script
- How to INSERT rows in a MySQL table from a Python script
- What ORM means, and how it abstracts storage away from usage
- How to map a Python class to a MySQL table with SQLAlchemy
- How to protect a query against SQL injection (parameterized queries vs.
  string formatting)

## Files

| File | Description |
|------|-------------|
| 0-select_states.py | List all states (MySQLdb) |
| 1-filter_states.py | List states starting with an uppercase N |
| 2-my_filter_states.py | Filter states by a user-supplied name (unsafe, for comparison) |
| 3-my_safe_filter_states.py | Same as above, safe from SQL injection |
| 4-cities_by_state.py | List all cities with their state (single JOIN query) |
| 5-filter_cities.py | List cities of a given state (safe from SQL injection) |
| model_state.py | SQLAlchemy State model, mapped to the states table |
| 6-model_state.py | Create the states table from the State model |
| 7-model_state_fetch_all.py | List all State objects (SQLAlchemy) |
| 8-model_state_fetch_first.py | Print the first State object |
| 9-model_state_filter_a.py | List all State objects containing the letter a |
| 10-model_state_my_get.py | Print a State's id by name, or "Not found" |
| 11-model_state_insert.py | Insert a new State ("Louisiana") |
| 12-model_state_update_id_2.py | Rename the State with id = 2 |
| 13-model_state_delete_a.py | Delete all States containing the letter a |
| model_city.py | SQLAlchemy City model, with a FOREIGN KEY to states |
| 14-model_city_fetch_by_state.py | List all cities with their state name |

## Author

engarambe-spec
