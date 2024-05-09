import random
import sympy

def generate_key_pair(p, q):
    n = p * q
    phi_n = (p - 1) * (q - 1)
    e = random.randint(2, phi_n - 1)
    while sympy.gcd(e, phi_n) != 1:
        e = random.randint(2, phi_n - 1)
    d = sympy.mod_inverse(e, phi_n)
    return ((e, n), (d, n), phi_n)

def coprime_public_keys(phi_n):
    return [e for e in range(2, phi_n) if sympy.gcd(e, phi_n) == 1]

def encrypt(message, public_key):
    e, n = public_key
    encrypted = [pow(ord(char), e, n) for char in message]
    return encrypted

def decrypt(ciphertext, private_key):
    d, n = private_key
    decrypted = [chr(pow(char, d, n)) for char in ciphertext]
    return "".join(decrypted)

# Step 1: Input values of p and q
p = int(input("Enter the value of p: "))
q = int(input("Enter the value of q: "))

# Step 2: Generate key pair
public_key, private_key, phi_n = generate_key_pair(p, q)

# Step 3: Input message
message = input("Enter the message to encrypt: ")

# Step 4: List all possible public keys which satisfy coprime condition
possible_public_keys = coprime_public_keys(phi_n)

# Step 5: Select any public key randomly to encrypt the input message
selected_public_key = random.choice(possible_public_keys)

# Step 6: Encrypt the message using the selected public key
encrypted_text = encrypt(message, (selected_public_key, public_key[1]))

# Step 7: Decrypt the ciphertext using the private key
decrypted_text = decrypt(encrypted_text, private_key)

# Step 8: Display input processed message
print("Input processed message:", message)

# Step 9: Display selected public key
print("Selected public key:", selected_public_key)

# Step 10: Display encrypted text
print("Encrypted text:", encrypted_text)

# Step 11: Display decrypted text
print("Decrypted text:", decrypted_text)
