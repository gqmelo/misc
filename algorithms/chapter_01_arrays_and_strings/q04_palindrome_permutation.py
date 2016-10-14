import collections


def is_palindrome_permutation(string):
    counter = collections.Counter(string)
    odd_counts = [v for v in counter.values() if v % 2 == 1]
    return len(odd_counts) <= 1
