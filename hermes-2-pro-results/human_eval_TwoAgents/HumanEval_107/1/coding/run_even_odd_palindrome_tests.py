# filename: run_even_odd_palindrome_tests.py

from my_tests import run_tests


def even_odd_palindrome(n):
    """
    Given a positive integer n, return a tuple that has the number of even and odd
    integer palindromes that fall within the range(1, n), inclusive.

    Example 1:

        Input: 3
        Output: (1, 2)
        Explanation:
        Integer palindrome are 1, 2, 3. one of them is even, and two of them are odd.

    Example 2:

        Input: 12
        Output: (4, 6)
        Explanation:
        Integer palindrome are 1, 2, 3, 4, 5, 6, 7, 8, 9, 11. four of them are even, and 6 of them are odd.

    Note:
        1. 1 <= n <= 10^3
        2. returned tuple has the number of even and odd integer palindromes respectively.
    """

    palindrome_counts = [0, 0]

    for i in range(1, n + 1):
        number = str(i)
        if number == number[::-1]:
            if i % 2 == 0:
                palindrome_counts[0] += 1
            else:
                palindrome_counts[1] += 1

    return palindrome_counts


# Run the unit tests
run_tests(even_odd_palindrome)