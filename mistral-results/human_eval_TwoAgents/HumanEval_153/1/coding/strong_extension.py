# filename: strong_extension.py
from collections import defaultdict
import re

def Strongest_Extension(class_name, extensions):
    """You will be given the name of a class (a string) and a list of extensions.
    The extensions are to be used to load additional classes to the class. The
    strength of an extension is given by the fraction CAP - SM where CAP is the number of 
    uppercase letters, and SM is the number of lowercase letters in the extension's name.
    You should find the strongest extension and return a string in this format:
        ClassName.StrongestExtensionName.
    If there are two or more extensions with the same strength, you should choose the one that comes first alphabetically in the list.
    For example, if you are given "my_class" as the class and a list of the extensions ['AA', 'be', 'CC'] then you should return 'my_class.AA' since 'AA' is the strongest extension (its strength is 1).
    """

    # Calculate strengths of all extensions
    strength_scores = defaultdict(float)

    for ext in extensions:
        cap_count, sm_count = 0, 0
        matched = re.match('[A-Z][a-z]*', ext)
        class_extended = f"{class_name}.{ext}"

        if matched:
            for char in matched.group():
                cap_count += (ord(char) - ord('A') + 1) if char.isupper() else 0
            sm_count = len(matched.group()[1:])

            strength_scores[class_extended] = cap_count - sm_count

    strongest_extension = max(strength_scores, key=lambda k: strength_scores[k])
    return strongest_extension

from my_tests import run_tests
run_tests(Strongest_Extension)