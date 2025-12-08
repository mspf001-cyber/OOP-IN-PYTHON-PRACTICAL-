"""Practical 02: Prime number operations using functions"""

import math

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def primes_till_n(n):
    return [i for i in range(2, n + 1) if is_prime(i)]

def first_n_primes(n):
    primes, num = [], 2
    while len(primes) < n:
        if is_prime(num):
            primes.append(num)
        num += 1
    return primes

n = int(input("Enter a number: "))
print(f"\n{n} is {'prime' if is_prime(n) else 'not prime'}")
print(f"Primes till {n}: {primes_till_n(n)}")
print(f"First {n} primes: {first_n_primes(n)}")