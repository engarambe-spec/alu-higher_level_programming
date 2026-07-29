# python-inheritance

This project covers inheritance in Python: superclasses, subclasses,
multiple inheritance, `isinstance`/`issubclass`/`type`/`super`, and
building a small class hierarchy (`BaseGeometry` -> `Rectangle` -> `Square`).

## Learning Objectives

- What is a superclass, baseclass or parentclass
- What is a subclass
- How to list all attributes and methods of a class or instance
- When can an instance have new attributes
- How to inherit a class from another
- How to define a class with multiple base classes
- What is the default class every class inherits from
- How to override a method or attribute inherited from the base class
- Which attributes or methods are available by heritage to subclasses
- What is the purpose of inheritance
- What are, when, and how to use `isinstance`, `issubclass`, `type`,
  and `super`

## Files

| File | Description |
|------|--------------|
| 0-lookup.py | `lookup(obj)` returns `dir(obj)` |
| 1-my_list.py | `MyList` class inheriting from `list`, with `print_sorted()` |
| tests/1-my_list.txt | Doctest for `MyList` |
| 2-is_same_class.py | `is_same_class(obj, a_class)` |
| 3-is_kind_of_class.py | `is_kind_of_class(obj, a_class)` |
| 4-inherits_from.py | `inherits_from(obj, a_class)` |
| 5-base_geometry.py | Empty `BaseGeometry` class |
| 6-base_geometry.py | `BaseGeometry` with `area()` raising an exception |
| 7-base_geometry.py | `BaseGeometry` with `integer_validator()` |
| tests/7-base_geometry.txt | Doctest for `BaseGeometry` |
| 8-rectangle.py | `Rectangle` with private, validated width/height |
| 9-rectangle.py | `Rectangle` with `area()` and `__str__` |
| 10-square.py | `Square` inheriting from `Rectangle` |
| 11-square.py | `Square` with its own `__str__` |

## Author

engarambe-spec
