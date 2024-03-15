# filename: complete_code.py
from my_tests import run_tests

def Strongest_Extension(class_name, extensions):
    """Extended function with full functionality."""
    def calculate_strength(extension):
        upper = sum(1 for letter in extension if letter.isupper())
        lower = sum(1 for letter in extension if letter.islower())
        return upper - lower

    strongest_extension = max(extensions, key=calculate_strength)
    return f"{class_name}.{strongest_extension}"

# Run the unit tests
run_tests(Strongest_Extension)