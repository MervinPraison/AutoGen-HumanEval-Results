# filename: complete_Strongest_Extension.py
from my_tests import run_tests

def Strongest_Extension(class_name, extensions):
    """
    Find the strongest extension based on the given formula and return a string.
    """
    strongest_extension = None
    highest_strength = float('-inf')  # initialize with negative infinity to ensure any strength is higher
    
    for extension in extensions:
        CAP = sum(1 for c in extension if c.isupper())
        SM = sum(1 for c in extension if c.islower())
        strength = CAP - SM
        
        if strength > highest_strength:
            strongest_extension = extension
            highest_strength = strength
    
    return f"{class_name}.{strongest_extension}"

# Run the unit tests
run_tests(Strongest_Extension)