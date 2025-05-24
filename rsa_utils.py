import sympy
import random

# Key Generation
def generate_keys():
    # Choose two distinct prime numbers
    p = sympy.randprime(100, 300)
    q = sympy.randprime(100, 300)
    while p == q:
        q = sympy.randprime(100, 300)

    n = p * q
    phi = (p - 1) * (q - 1)

    # Choose e such that it is coprime with phi and 1 < e < phi
    e = random.randrange(2, phi)
    while sympy.gcd(e, phi) != 1:
        e = random.randrange(2, phi)

    # Compute d, the modular inverse of e
    d = sympy.mod_inverse(e, phi)

    return (e, n), (d, n)


# Encryption 
def encrypt(message, public_key):
    e, n = public_key
    cipher = [pow(ord(char), e, n) for char in message]
    return cipher


# Decryption
def decrypt(cipher, private_key):
    d, n = private_key
    plain = [chr(pow(char, d, n)) for char in cipher]
    return ''.join(plain)
