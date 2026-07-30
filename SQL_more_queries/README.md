# SQL_more_queries

This project builds on SQL fundamentals by covering MySQL user
management and privileges, table constraints (NOT NULL, UNIQUE,
DEFAULT, PRIMARY KEY, FOREIGN KEY), and multi-table queries using
subqueries, JOIN, and LEFT JOIN.

## Learning Objectives

- How to create a new MySQL user
- How to manage privileges for a user on a database or table
- What a PRIMARY KEY is
- What a FOREIGN KEY is
- How to use NOT NULL and UNIQUE constraints
- How to retrieve data from multiple tables in one request
- What subqueries are
- What JOIN and UNION are

## Requirements

- Scripts are run against MySQL 8.0 on Ubuntu 20.04 LTS
- Every file starts with a comment describing the task
- Every SQL statement has a comment on the line(s) just above it
- All SQL keywords are in uppercase
- Every file ends with a new line

## Files

| File | Description |
|------|-------------|
| 0-privileges.sql | Lists all privileges of user_0d_1 and user_0d_2 |
| 1-create_user.sql | Creates user_0d_1 with all privileges |
| 2-create_read_user.sql | Creates hbtn_0d_2 db + read-only user_0d_2 |
| 3-force_name.sql | Table force_name, name can't be NULL |
| 4-never_empty.sql | Table id_not_null, id defaults to 1 |
| 5-unique_id.sql | Table unique_id, id defaults to 1 and is UNIQUE |
| 6-states.sql | Database hbtn_0d_usa + table states (PK id) |
| 7-cities.sql | Table cities (FK state_id -> states.id) |
| 8-cities_of_california_subquery.sql | Cities of CA, via subquery, no JOIN |
| 9-cities_by_state_join.sql | All cities with their state name, via JOIN |
| 10-genre_id_by_show.sql | Shows with at least one genre linked |
| 11-genre_id_all_shows.sql | All shows, genre_id NULL if none linked |
| 12-no_genre.sql | Shows with no genre linked |
| 13-count_shows_by_genre.sql | Number of shows per genre, desc by count |
| 14-my_genres.sql | All genres of the show Dexter |
| 15-comedy_only.sql | All shows in the Comedy genre |
| 16-shows_by_genre.sql | All shows + genres, NULL if none, via LEFT JOIN |

## Notes

Tasks 10-16 require importing the `hbtn_0d_tvshows` database dump
provided in the project resources before running those scripts:
