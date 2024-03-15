# filename: complete_even_odd_palindrome.py
from my_tests import run_tests

def even_odd_palindrome(n):
    """
    Given a positive integer n, return a tuple that has the number of even and odd
    integer palindromes that fall within the range(1, n), inclusive.
    """
    def is_palindrome(num):
        return str(num) == str(num)[::-1]

    even_count, odd_count = 0, 0
    for i in range(1, n + 1):
        if is_palindrome(i):
            if i % 2 == 0:
                even_count += 1
            else:
                odd_count += 1
    return (even_count, odd_count)

# Run the unit tests
run_tests(even_odd_palindrome)