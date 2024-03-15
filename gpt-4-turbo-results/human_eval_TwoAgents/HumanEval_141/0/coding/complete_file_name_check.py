# filename: complete_file_name_check.py
from my_tests import run_tests

def file_name_check(file_name):
    """
    Create a function which takes a string representing a file's name, and returns
    'Yes' if the the file's name is valid, and returns 'No' otherwise.
    A file's name is considered to be valid if and only if all the following conditions 
    are met:
    - There should not be more than three digits ('0'-'9') in the file's name.
    - The file's name contains exactly one dot '.'
    - The substring before the dot should not be empty, and it starts with a letter from 
    the latin alphapet ('a'-'z' and 'A'-'Z').
    - The substring after the dot should be one of these: ['txt', 'exe', 'dll']
    """
    # Check for more than three digits
    digits_count = sum(c.isdigit() for c in file_name)
    if digits_count > 3:
        return 'No'
    
    # Check for exactly one dot
    if file_name.count('.') != 1:
        return 'No'
    
    # Split the file name by dot
    name, extension = file_name.split('.')
    
    # Check if name starts with a latin alphabet letter and is not empty
    if not name or not name[0].isalpha():
        return 'No'
    
    # Check if the extension is one of the valid options
    if extension not in ['txt', 'exe', 'dll']:
        return 'No'
    
    return 'Yes'

# Run the unit tests
run_tests(file_name_check)