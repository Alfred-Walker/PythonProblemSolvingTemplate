"""Eratosthenes' sieve examples to find prime number between M, N (M <= p <= N)

Python math module documentation:
   https://docs.python.org/3.8/library/math.html
"""

import sys


# arbitrary upper bound
M, N = map(int, sys.stdin.readline().rstrip().split())

# arbitrary upper bound
is_prime_number = [True] * 1000001

# 1 is not a prime number
is_prime_number[1] = False


# find prime numbers by excluding multiple of prime numbers
for i in range(2, int(N ** 0.5) + 1):
    if is_prime_number[i]:
        for j in range(i * i, N + 1, i):
            is_prime_number[j] = False
            j += i


prime_numbers = []

# get prime numbers between M and N
for i in range(M, N + 1):
    if is_prime_number[i]:
        prime_numbers.append(i)

print(prime_numbers)
# >> 3 19
# >> [3, 5, 7, 11, 13, 17, 19]
