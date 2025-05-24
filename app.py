# Console Interface

import rsa_utils

def main():
    print("🔐 RSA Encryption/Decryption Tool")

    # Key generation
    public_key, private_key = rsa_utils.generate_keys()
    print(f"\nPublic Key: {public_key}")
    print(f"Private Key: {private_key}")

    # Input message
    message = input("\nEnter a message to encrypt: ")
    cipher = rsa_utils.encrypt(message, public_key)
    print(f"\n🔒 Encrypted Message: {cipher}")

    # Decrypt
    decrypted = rsa_utils.decrypt(cipher, private_key)
    print(f"\n🔓 Decrypted Message: {decrypted}")


if __name__ == "__main__":
    main()
