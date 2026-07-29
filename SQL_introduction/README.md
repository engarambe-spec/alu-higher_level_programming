# SQL_introduction

This project covers the basics of relational databases and SQL using
MySQL 8.0: creating and dropping databases, creating tables, and using
core DDL/DML statements (CREATE, INSERT, SELECT, UPDATE, DELETE) along
with simple aggregation (COUNT, AVG, GROUP BY).

## Learning Objectives

- What's a database, and what's a relational database
- What SQL stands for, and what MySQL is
- How to create a database in MySQL
- What DDL and DML stand for
- How to CREATE or ALTER a table
- How to SELECT data from a table
- How to INSERT, UPDATE, or DELETE data
- What subqueries are
- How to use MySQL functions (COUNT, AVG)

## Requirements

- Scripts are run against MySQL 8.0 on Ubuntu 20.04 LTS
- Every file starts with a comment describing the task
- Every SQL statement has a comment on the line(s) just above it
- All SQL keywords are in uppercase
- Every file ends with a new line

## Files

| File | Description |
|------|-------------|
| 0-list_databases.sql | Lists all databases |
| 1-create_database_if_missing.sql | Creates `hbtn_0c_0` if missing |
| 2-remove_database.sql | Drops `hbtn_0c_0` if it exists |
| 3-list_tables.sql | Lists all tables of a database |
| 4-first_table.sql | Creates `first_table` (id INT, name VARCHAR(256)) |
| 5-full_table.sql | Prints full description of `first_table` |
| 6-list_values.sql | Lists all rows of `first_table` |
| 7-insert_value.sql | Inserts id=89, name="Best School" |
| 8-count_89.sql | Counts records with id = 89 |
| 9-full_creation.sql | Creates `second_table` and inserts 4 records |
| 10-top_score.sql | Lists all records ordered by score (desc) |
| 11-best_score.sql | Lists records with score >= 10 |
| 12-no_cheating.sql | Updates Bob's score to 10, by name only |
| 13-change_class.sql | Deletes records with score <= 5 |
| 14-average.sql | Computes the average score |
| 15-groups.sql | Counts records per score, ordered by count desc |
| 16-no_link.sql | Lists records with a name, ordered by score desc |

## How to run
(The database name is passed as an extra argument for scripts that
operate on a specific database's tables.)

## Author

qshejantab-byte
