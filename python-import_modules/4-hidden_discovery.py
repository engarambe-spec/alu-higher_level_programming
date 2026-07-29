#!/usr/bin/python3
"""Program that prints all names defined by hidden_4.pyc"""

if __name__ == "__main__":
    import hidden_4
    for name in sorted(dir(hidden_4)):
        if not name.startswith("__"):
            print(name)
