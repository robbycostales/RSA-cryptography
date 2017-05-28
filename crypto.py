#
# Author: Robert Costales
# Date: 2017 05 26
# Language: Python 3
# Purpose: Create encrypt and dycrypt functions for RSA method.
#

import fractions
import time
import numpy
import random
from math import sqrt
from itertools import count, islice


def roll_mult(number, times, maxnum):
    """
    Multiplies a number by itself a number of times, and it rolls over when it
    hits the max value

    Args:
        number : number that will be multiplied by itself
        times : number of times that the number will be multiplied by itself
        maxnum : max value that will prompt the roll-over
    """
    # n : value counter
    n = 1
    for i in range(times):
        n = (n * number ) % maxnum
    return n


def EEA(b, n):
    """
    Extended Euclidean Algorithm
    Note : phin -> phi(n)
    b x0 + phin y0 = g = gcd(b,phin)

    Args:
        b : e = public key
        n : phi (n) = Euler's totient function of the product of the two
                primes

    Returns:
        b : gcd
        x0 : private key
        y0 : no significance for our purposes


    """
    x0, x1, y0, y1 = 1, 0, 0, 1
    while n != 0:
        q, b, n = b // n, n, b % n
        x0, x1 = x1, x0 - q * x1
        y0, y1 = y1, y0 - q * y1
    return  b, x0, y0


def phi(n):
    """
    Euler's Totient Function
    """
    amount = 0
    for k in range(1, n + 1):
        if fractions.gcd(n, k) == 1:
            amount += 1
    return amount


def get_priv_key(pub, maxnum):
    """
    Gets private key based on public key, and maxnum (N)

    Args:
        pub : public key
        maxnum : N

    Returns:
        private key
    """
    phin = phi(maxnum)
    priv = EEA(pub, phin)[1]


def isPrime(n):
    """
    Tests if a number is prime
    """
    if n < 2: return False
    for number in islice(count(2), int(sqrt(n)-1)):
        if not n%number:
            return False
    return True


def encrypt(inp, out, min_prime=0, max_prime=100):
    """
    Encrypts a piece of text using RSA method

    Args:
        inp : input text file
        out : output text file, where encrypted text will exist

    Returns: decryption key
    """
    # initialising primes
    cached_primes = [i for i in range(min_prime,max_prime) if isPrime(i)]
    # n : choose random prime from list
    n = random.choice(cached_primes)

    # obtain list of letters from text file
    chars = []

    key = 4
    return key


def decrypt(inp, out):
    """
    Decrypts a piece of input

    Args:
        inp : input text file
        out : output text file, where decrypted text will exist
    """
