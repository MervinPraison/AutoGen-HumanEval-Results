# filename: complete_code.py
from my_tests import run_tests

def file_name_check(file_name):
    """Create a function which takes a string representing a file's name, and returns
    'Yes' if the file's name is valid, and returns 'No' otherwise.
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
    # Check for the number of dots and split the filename
    if file_name.count('.') != 1:
        return 'No'
    name, extension = file_name.rsplit('.', 1)

    # Check if the name starts with a letter and does not have more than 3 digits
    if not name[0].isalpha() or len([char for char in name if char.isdigit()]) > 3:
        return 'No'

    # Check if the extension is one of the allowed ones
    if extension not in ['txt', 'exe', 'dll']:
        return 'No'

    return 'Yes'

# Run the unit tests
run_tests(file_name_check)