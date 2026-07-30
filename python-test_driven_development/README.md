# python-test_driven_development

This project covers Test Driven Development (TDD) in Python: writing
interactive doctests before/alongside implementation, using the
`doctest` module to validate code from documentation, and writing
`unittest`-based unit tests for a function.

## Learning Objectives

- Why Python programming is awesome
- What an interactive test is
- Why tests are important
- How to write docstrings to create tests
- How to write documentation for each module and function
- What the basic option flags for creating tests are
- How to find edge cases

## Requirements

- Every file starts with exactly `#!/usr/bin/python3`
- Code follows pycodestyle (2.7.*)
- Every file is executable and ends with a new line
- All doctest files live inside `tests/` as `.txt` files, run with
  `python3 -m doctest ./tests/*`
- The unittest file lives inside `tests/` as a `.py` file, run with
  `python3 -m unittest tests.6-max_integer_test`
- Every module and function has a real, descriptive docstring

## Files

| File | Description |
|------|-------------|
| 0-add_integer.py | Adds two integers/floats, casting floats to int |
| tests/0-add_integer.txt | Doctest for add_integer |
| 2-matrix_divided.py | Divides all elements of a matrix by a number |
| tests/2-matrix_divided.txt | Doctest for matrix_divided |
| 3-say_my_name.py | Prints "My name is `<first>` `<last>`" |
| tests/3-say_my_name.txt | Doctest for say_my_name |
| 4-print_square.py | Prints a square using the `#` character |
| tests/4-print_square.txt | Doctest for print_square |
| 5-text_indentation.py | Prints text with extra newlines after `. ? :` |
| tests/5-text_indentation.txt | Doctest for text_indentation |
| 6-max_integer.py | Finds the max integer in a list |
| tests/6-max_integer_test.py | Unittest suite for max_integer |

## Testing

Every doctest file was run and verified to pass in full:
## Author

qshejantab-byte
