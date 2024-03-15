# filename: complete_code.py
from my_tests import run_tests


def right_angle_triangle(a, b, c):
    '''
    Given the lengths of the three sides of a triangle. Return True if the three
    sides form a right-angled triangle, False otherwise.
    A right-angled triangle is a triangle in which one angle is right angle or 
    90 degree.
    Example:
    right_angle_triangle(3, 4, 5) == True
    right_angle_triangle(1, 2, 3) == False
    '''
    # Sorting the sides ensures the largest (potential hypotenuse) is last
    sides = sorted([a, b, c])
    # Checking the Pythagorean theorem
    return sides[0]**2 + sides[1]**2 == sides[2]**2

# Run the unit tests
run_tests(right_angle_triangle)