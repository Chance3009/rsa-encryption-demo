import sympy
import random


# --- Key Generation ---
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


# --- Encryption ---
def encrypt(message, public_key):
    e, n = public_key
    cipher = [pow(ord(char), e, n) for char in message]
    return cipher


# --- Decryption ---
def decrypt(cipher, private_key):
    d, n = private_key
    plain = [chr(pow(char, d, n)) for char in cipher]
    return ''.join(plain)


# --- Console Interface ---
def main():
    print("🔐 RSA Encryption/Decryption Tool")

    # Key generation
    public_key, private_key = generate_keys()
    print(f"\nPublic Key: {public_key}")
    print(f"Private Key: {private_key}")

    # Input message
    message = input("\nEnter a message to encrypt: ")
    cipher = encrypt(message, public_key)
    print(f"\n🔒 Encrypted Message: {cipher}")

    # Decrypt
    decrypted = decrypt(cipher, private_key)
    print(f"\n🔓 Decrypted Message: {decrypted}")


if __name__ == "__main__":
    main()
