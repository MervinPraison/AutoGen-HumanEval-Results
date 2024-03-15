# filename: complete_code.py
from my_tests import run_tests

def file_name_check(file_name):
    # Check for the number of digits in the file name
    if sum(c.isdigit() for c in file_name) > 3:
        return 'No'
    
    # Check for exactly one dot '.'
    if file_name.count('.') != 1:
        return 'No'
    
    # Split the file name on the dot
    name_part, extension_part = file_name.split('.')
    
    # Check if the name part is not empty and starts with a letter
    if not name_part or not name_part[0].isalpha():
        return 'No'
    
    # Check if the extension is one of the allowed options
    if extension_part not in ['txt', 'exe', 'dll']:
        return 'No'
    
    # If all conditions are met, return 'Yes'
    return 'Yes'

# Run the unit tests
run_tests(file_name_check)