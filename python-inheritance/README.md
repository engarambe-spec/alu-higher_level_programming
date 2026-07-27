# python-inheritance

This project covers inheritance in Python: introspection with `dir()`,
`isinstance()` vs `type()` checks, and building a small shape hierarchy
(`BaseGeometry` -> `Rectangle` -> `Square`) with private attributes and
custom validation.

## Learning Objectives

- What is `dir()` used for, and how does inspection with `lookup()` work
- Difference between `type(obj) is a_class`, `isinstance()`, and true
  inheritance checks (`inherits_from`)
- Overloading `__init__` and calling `super()` correctly
- Raising `TypeError` / `ValueError` from a shared validator method
- Private attributes and name-mangling across a class hierarchy
- Implementing `__str__` for custom print behavior

## Files

| File | Description |
|------|-------------|
| 0-lookup.py | Returns available attributes/methods of an object |
| 1-my_list.py | `MyList(list)` with `print_sorted()` |
| tests/1-my_list.txt | Doctest for MyList |
| 2-is_same_class.py | Checks exact class match |
| 3-is_kind_of_class.py | Checks `isinstance` (class or subclass) |
| 4-inherits_from.py | Checks strict subclass inheritance |
| 5-base_geometry.py | Empty `BaseGeometry` class |
| 6-base_geometry.py | `BaseGeometry` with `area()` raising Exception |
| 7-base_geometry.py | Adds `integer_validator()` |
| tests/7-base_geometry.txt | Doctest for `integer_validator` |
| 8-rectangle.py | `Rectangle(BaseGeometry)`, private width/height |
| 9-rectangle.py | Adds `area()` and `__str__` |
| 10-square.py | `Square(Rectangle)`, area only |
| 11-square.py | Adds `__str__` returning `[Square] w/h` |

## Author

qshejantab-byte
