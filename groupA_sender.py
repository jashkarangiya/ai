import hashlib
import random

def caesar_cipher(text, key):
    result = ''
    for char in text:
        if char.isalpha():
            shift = 65 if char.isupper() else 97
            result += chr((ord(char) - shift + key) % 26 + shift)
        else:
            result += char
    return result

def generate_key():
    return random.randint(1, 26)

def calculate_hash(text):
    return hashlib.sha256(text.encode()).hexdigest()

def main():
    # Step 1: Sender enters plaintext
    plaintext_filename = input("Enter the name of the plaintext file: ")

    # Step 2: Load plaintext
    with open(plaintext_filename, 'r') as file:
        plaintext = file.read()

    # Step 3: Generate and store key
    key = generate_key()
    with open('KEY.TXT', 'w') as key_file:
        key_file.write(str(key))

    # Step 4: Encrypt plaintext
    cipher_text = caesar_cipher(plaintext, key)
    with open('cipher.txt', 'w') as cipher_file:
        cipher_file.write(cipher_text)

    # Step 5: Calculate hash
    hash_code = calculate_hash(cipher_text)

    # Step 6: Send hashcode along with cipher text
    with open('cipher.txt', 'a') as cipher_file:
        cipher_file.write('\n')
        cipher_file.write(hash_code)

    print("Cipher text and hash code saved successfully.")

if __name__ == "__main__":
    main()

