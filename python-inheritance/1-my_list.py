
#!/usr/bin/python3

"""Module that defines a class MyList."""





class MyList(list):

    """Represents a list, extended with a sorted-print method."""



    def print_sorted(self):

        """Prints the list, sorted in ascending order."""

        print(sorted(self))

