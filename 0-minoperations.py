#!/usr/bin/python3
"""
Minimum operations required to archieve a certain number of characters.
"""


def minOperations(n):
    """Returns the minimum operations required to archieve n characters."""
    if n <= 1:
        return 0
    else:
        for i in range(2, n + 1):
            if n % i == 0:
                return minOperations(n // i) + i
        return n


if __name__ == "__main__":
    n = 4
    print(
        "Min # of operations to reach {} char: {}".format(n, minOperations(n))
            )

    n = 12
    print(
        "Min # of operations to reach {} char: {}".format(n, minOperations(n))
            )
