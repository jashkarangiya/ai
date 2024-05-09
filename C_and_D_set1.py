import random
import sympy

def generate_key_pair(p, q):
    """Generates a public/private key pair using RSA algorithm.

    Args:
        p (int): First prime number.
        q (int): Second prime number.

    Returns:
        tuple: A tuple containing the public key (e, n) and private key (d, n).
    """

    n = p * q
    phi_n = (p - 1) * (q - 1)
    e = random.randint(2, phi_n - 1)
    while sympy.gcd(e, phi_n) != 1:
        e = random.randint(2, phi_n - 1)
    d = sympy.mod_inverse(e, phi_n)
    return ((e, n), (d, n))

def coprime_public_keys(phi_n):
    """Finds all coprime public keys (e) for a given phi_n.

    Args:
        phi_n (int): Euler's totient function of n.

    Returns:
        list: A list of all coprime public keys (e) for the given phi_n.
    """

    return [e for e in range(2, phi_n) if sympy.gcd(e, phi_n) == 1]

def encrypt(message, public_key):
    """Encrypts a message using RSA algorithm.

    Args:
        message (str): The message to encrypt.
        public_key (tuple): The public key (e, n).

    Returns:
        list: A list of encrypted message blocks.
    """

    e, n = public_key
    encrypted = [pow(ord(char), e, n) for char in message]
    return encrypted

def decrypt(ciphertext, private_key):
    """Decrypts an encrypted message using RSA algorithm.

    Args:
        ciphertext (list): The list of encrypted message blocks.
        private_key (tuple): The private key (d, n).

    Returns:
        str: The decrypted message.
    """

    d, n = private_key
    decrypted = [pow(char, d, n) for char in ciphertext]
    decrypted_chars = [chr(char) for char in decrypted if 0 <= char < 128]  # Filter out invalid ASCII values
    return ''.join(decrypted_chars)

def main():
    """Generates keys, encrypts and decrypts a message."""

    # Step 1: Input values of p and q
    while True:
        try:
            p = int(input("Enter the value of p (prime number): "))
            q = int(input("Enter the value of q (prime number): "))
            if sympy.isprime(p) and sympy.isprime(q):
                break
            else:
                print("p and q must be prime numbers. Please try again.")
        except ValueError:
            print("Invalid input. Please enter integers.")

    # Step 2: Generate key pair
    public_key, private_key = generate_key_pair(p, q)

    # Step 3: Input message
    message = input("Enter the message to encrypt: ")

    # Step 4: No need to find all possible public keys (redundant)

    # Step 5: Encrypt the message using the public key
    encrypted_text = encrypt(message, public_key)

    # Step 6: Decrypt the ciphertext using the private key
    decrypted_text = decrypt(encrypted_text, private_key)

    # Step 7: Display results
    print("Input message:", message)
    print("Encrypted text:", encrypted_text)
    print("Decrypted text:", decrypted_text)

if __name__ == "__main__":
    main()
