# filename: improved_completion_fixed.py
import re

valid_extensions = ['txt', 'exe', 'dll'] # Update valid_extensions

def file_name_check(file_name):
    """Create a function which takes a string representing a file's name, and returns
    'Yes' if the the file's name is valid, and returns 'No' otherwise.
    """
    try:
        if len(file_name) == 0:
            return 'No'

        name_before_extension = file_name[:file_name.rfind('.')] if '.' in file_name else file_name
        regex = re.compile(r"[a-zA-Z0-9_\+]+") # Update regex to allow underscores, alphanumeric characters and '+' sign
        if not regex.match(name_before_extension):
            print(f"Invalid name before extension in file_name '{file_name}'")
            raise ValueError("Invalid name before extension")

        extensions = re.findall(r"([.\w]+)$", file_name) # Match valid extensions at the end of a string (using a character class \w for alphanumeric characters)

        if len(extensions) != 1 or extensions[0] not in valid_extensions:
            print(f"File name '{file_name}' has an invalid extension '{extensions[0]}'")
            raise ValueError(f"Invalid extension '{extensions[0]}'")

        # If all conditions are met, return 'Yes'
        return 'Yes'
    except Exception as e:
        print(f"Error in file_name_check: {e}")
        return 'No'

def test_file_name_check():
    """Create a function to test file_name_check function. Add as many test cases as needed."""

    test_cases = [("myFile.txt", "Yes"), ("invalidName+1.dll", "No"), ("missingExtension.asd", "No")]

    for case in test_cases:
        result = file_name_check(case[0])
        assert result == case[1], f"Error: {result} != {case[1]} for file_name '{case[0]}'"

# Run the tests
test_file_name_check()