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
        n = (n * number) % maxnum
    return n


def EEA(b, n):
    # THIS FUNCTION DOES NOT WORK
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


def try_priv_key(pub, maxnum):
    phin = phi(maxnum)
    count = 1
    print("Working on finding private key...")
    while (pub*count) % phin !=1:
        count +=1
    return count


def get_priv_key(pub, maxnum):
    # THIS FUNCTION DOES NOT WORK
    """
    Gets private key based on public key, and maxnum (N)

    Args:
        pub : public key
        maxnum : N

    Returns:
        private key
    """
    phin = phi(maxnum)
    z, priv, a = EEA(pub, phin)
    print(z, priv, a)
    print("priv:", priv)
    return priv


def isPrime(n):
    """
    Tests if a number is prime
    """
    if n < 2: return False
    for number in islice(count(2), int(sqrt(n)-1)):
        if not n%number:
            return False
    return True


def file_to_list(fyle):
    """
    Converts .txt to list of characters to encrypt

    Args:
        fyle : file to convert
    Returns:
        list
    """
    new_list = []
    with open(fyle) as f:
        while True:
            c = f.read(1)
            if not c:
                break
            new_list.append(c)
    return new_list


def encrypt(inp, out, min_prime, max_prime):
    """
    Encrypts a piece of text using RSA method

    Args:
        inp : input text file
        out : output text file, where encrypted text will exist
        min_prime : minimum prime number allowed
        max_prime : maximum prime number allowed

    Returns: decryption key
    """
    # initialising primes
    cached_primes = [i for i in range(min_prime,max_prime) if isPrime(i)]
    # p,q : choose random prime from list
    p = random.choice(cached_primes)
    q = random.choice(cached_primes)
    # This is the limit
    N = p*q
    phin = phi(N)
    # public key
    e = 7

    # obtain list of letters from text file
    og_characters = file_to_list(inp)
    # og txt to nums
    og_nums = []
    for i in og_characters:
        og_nums.append(ord(i))
    # og nums to new nums
    new_nums = []
    for i in og_nums:
        x = roll_mult(i, e, N)
        new_nums.append(x)
    # new nums to out file
    thefile = open(out, 'w')
    for item in new_nums:
        thefile.write("%s\n" % item)

    # find key
    key = try_priv_key(e, N)
    return key, N

def decrypt(inp, out, key, maxnum):
    """
    Decrypts a piece of input

    Args:
        inp : input text file
        out : output text file, where decrypted text will exist
    """
    # read encrypted file
    with open (inp, "r") as ins:
        array = []
        for line in ins:
            array.append(int(line[0:-1]))
    # convert back to og nums using key
    og_nums = []
    for i in array:
        x = roll_mult(i, key, maxnum)
        og_nums.append(x)
    # convert og nums to og chars
    og_chars = []
    for i in og_nums:
        x = chr(i)
        og_chars.append(x)

    thefile = open(out, 'w')
    for item in og_chars:
        thefile.write("%s" % item)
