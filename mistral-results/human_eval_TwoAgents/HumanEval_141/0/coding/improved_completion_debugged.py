# filename: improved_completion_debugged.py
from my_tests import run_tests
import re

valid_extensions = ['txt', 'exe', 'dll']

def file_name_check(file_name):
    """Create a function which takes a string representing a file's name, and returns
    'Yes' if the the file's name is valid, and returns 'No' otherwise.
    """

    try:
        if len(file_name) == 0:
            print(f"Empty file name '{file_name}'")
            return 'No'

        # Check for substring before the first dot (if present)
        name_before_extension = file_name[:file_name.index('.')]
        if not re.match(r'[a-zA-Z]\w*', name_before_extension) or len(name_before_extension) == 0:
            print(f"Invalid name before extension in file_name '{file_name}'")
            raise ValueError("Invalid name before extension")

        # Check for extensions (if any)
        extensions = [ext[1:] for ext in re.findall(r'\.(?!\.)[^./]+', file_name)]

        if len(extensions) != 0 and len(extensions) > len(valid_extensions):
            print(f"File name '{file_name}' has more extensions than expected: {extensions}")
            raise ValueError("Too many extensions")

        for extension in extensions:
            if extension not in valid_extensions:
                print(f"Invalid extension '{extension}' in file_name '{file_name}'")
                raise ValueError(f"Invalid extension '{extension}'")

        # If all conditions are met, return 'Yes'
        return 'Yes'
    except Exception as e:
        print(f"Error in file_name_check: {e}")
        return 'No'

# Run the unit tests
run_tests(file_name_check)