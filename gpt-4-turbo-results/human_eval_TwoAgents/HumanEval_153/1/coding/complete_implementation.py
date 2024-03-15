# filename: complete_implementation.py
from my_tests import run_tests

def Strongest_Extension(class_name, extensions):
    def extension_strength(extension):
        uppercase_count = sum(1 for c in extension if c.isupper())
        lowercase_count = sum(1 for c in extension if c.islower())
        return uppercase_count - lowercase_count

    strongest_extension = max(extensions, key=lambda ext: (extension_strength(ext), -extensions.index(ext)))
    return f"{class_name}.{strongest_extension}"

# Run the unit tests
run_tests(Strongest_Extension)