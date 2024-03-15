# filename: updated_completion.py
from my_tests import run_tests
import re

def file_name_check(file_name):
    """Create a function which takes a string representing a file's name, and returns
    'Yes' if the the file's name is valid, and returns 'No' otherwise.
    """

    try:
        # Check for substring before the dot
        if not re.match(r'[a-zA-Z]\w*', file_name[:file_name.index('.')]) or \
           len(file_name[:file_name.index('.')]) == 0:
            raise ValueError("Invalid name before extension")

        # Check for substring after the dot
        valid_extensions = ['txt', 'exe', 'dll']
        extension = file_name[file_name.index('.'):].lower()
        if len(extension) > len(valid_extensions):
            raise ValueError("Too many extensions")
        elif extension not in valid_extensions or \
             (len(extension) == 0 and len(valid_extensions) != 0):
            raise ValueError("Invalid extension")

        # If all conditions are met, return 'Yes'
        return 'Yes'
    except Exception as e:
        print(f"Error in file_name_check: {e}")
        return 'No'

# Run the unit tests
run_tests(file_name_check)