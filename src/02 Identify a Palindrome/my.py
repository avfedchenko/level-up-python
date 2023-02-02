import doctest
from string import ascii_letters


def is_palindrome(s):
    """Check that s is palindrome.
    >>> is_palindrome('hello world')
    False
    >>> is_palindrome('Go hang a salami, I’m a lasagna hog.')
    True
    """
    filtered = [letter for letter in s.lower() if letter in ascii_letters]
    return filtered == filtered[::-1]


doctest.testmod()
