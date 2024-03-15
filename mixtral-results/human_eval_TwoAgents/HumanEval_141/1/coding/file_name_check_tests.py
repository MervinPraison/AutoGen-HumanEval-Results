# filename: file_name_check_tests.py

import re
from my_tests import run_tests

def file_name_check(file_name):
    """Create a function which takes a string representing a file's name, and returns
    'Yes' if the the file's name is valid, and returns 'No' otherwise.
    A file's name is considered to be valid if and only if all the following conditions 
    are met:
    - There should not be more than three digits ('0'-'9') in the file's name.
    - The file's name contains exactly one dot '.'
    - The substring before the dot should not be empty, and it starts with a letter from 
    the latin alphapet ('a'-'z' and 'A'-'Z').
    - The substring after the dot should be one of these: ['txt', 'exe', 'dll']
    Examples:
    file_name_check("example.txt") # => 'Yes'
    file_name_check("1example.dll") # => 'No' (the name should start with a latin alphapet letter)
    """
    if not re.match(r'^[a-zA-Z][a-zA-Z0-9]*\.[a-zA-Z]{3}$', file_name):
        return 'No'
    dot_index = file_name.rindex('.')
    if dot_index < len(file_name) - 4 or dot_index == 0:
        return 'No'
    substring_after_dot = file_name[dot_index + 1:]
    if substring_after_dot not in ['txt', 'exe', 'dll']:
        return 'No'
    return 'Yes'

# Run the unit tests
run_tests(file_name_check)