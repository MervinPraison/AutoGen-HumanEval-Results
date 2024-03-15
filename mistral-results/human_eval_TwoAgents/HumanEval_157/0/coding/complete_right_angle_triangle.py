# filename: complete_right_angle_triangle.py

from my_tests import run_tests
import math

def right_angle_triangle(a, b, c):
    '''
    Given the lengths of the three sides of a triangle. Return True if the three
    sides form a right-angled triangle, False otherwise.
    A right-angled triangle is a triangle in which one angle is right angle or 90 degree.
    Example:
    right_angle_triangle(3, 4, 5) == True
    right_angle_triangle(1, 2, 3) == False
    '''
    hypotenuse = math.sqrt(a**2 + b**2)
    return (math.isclose(hypotenuse, a, rel_tol=0.001) and
            math.isclose(hypotenuse, c, rel_tol=0.001))

def main():
    # Run the unit tests and print failed test cases' inputs and results
    for test_case in run_tests(right_angle_triangle):
        if not test_case[1]:  # Check if the test case failed
            print(f"Test Case Input: ({test_case[0]}, {test_case[1]}, {test_case[2]})")
            print("Expected Result:", test_case[3])
            print("Actual Result:", right_angle_triangle(*test_case[:3]))
    print("All tests passed if no output is shown.")

if __name__ == '__main__':
    main()