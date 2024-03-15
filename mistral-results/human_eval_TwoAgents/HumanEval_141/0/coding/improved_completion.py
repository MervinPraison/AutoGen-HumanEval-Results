# filename: improved_completion.py
from my_tests import run_tests
import re

def file_name_check(file_name):
    """Create a function which takes a string representing a file's name, and returns
    'Yes' if the the file's name is valid, and returns 'No' otherwise.
    """

    try:
        # Check for substring before the first dot (if present)
        if not re.match(r'[a-zA-Z]\w*', file_name[:file_name.index('.')]) or \
           len(file_name[:file_name.index('.')]) == 0:
            raise ValueError("Invalid name before extension")

        # Check for extensions (if any)
        extensions = [ext[1:] for ext in re.findall(r'\.(?!\.)[^./]+', file_name)]
        if len(extensions) > len(valid_extensions):
            raise ValueError("Too many extensions")

        # Check each extension individually
        for extension in extensions:
            if extension not in valid_extensions:
                raise ValueError(f"Invalid extension '{extension}'")

        # If all conditions are met, return 'Yes'
        return 'Yes'
    except Exception as e:
        print(f"Error in file_name_check: {e}")
        return 'No'

# Run the unit tests
run_tests(file_name_check)