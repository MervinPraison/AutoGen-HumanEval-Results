# filename: completion.py
from my_tests import run_tests
import re

def file_name_check(file_name):
    """Create a function which takes a string representing a file's name, and returns
    'Yes' if the the file's name is valid, and returns 'No' otherwise.
    """

    # Check for substring before the dot
    if not re.match(r'[a-zA-Z]\w*', file_name[:file_name.index('.')]) or \
       len(file_name[:file_name.index('.')]) == 0:
        return 'No'

    # Check for substring after the dot
    valid_extensions = ['txt', 'exe', 'dll']
    extension = file_name[file_name.index('.'):].lower()
    if extension not in valid_extensions or len(extension) > 0 and extension[0] != '.':
        return 'No'

    # If all conditions are met, return 'Yes'
    return 'Yes'

# Run the unit tests
run_tests(file_name_check)