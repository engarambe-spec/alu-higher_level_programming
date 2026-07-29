#!/usr/bin/python3
"""Script that adds all arguments to a list and saves them to a file"""
from sys import argv
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

if __name__ == "__main__":
    filename = "add_item.json"
    try:
        my_list = load_from_json_file(filename)
    except Exception:
        my_list = []

    my_list.extend(argv[1:])

    save_to_json_file(my_list, filename)
