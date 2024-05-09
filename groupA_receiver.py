import hashlib

def caesar_cipher(text, key):
    result = ''
    for char in text:
        if char.isalpha():
            shift = 65 if char.isupper() else 97
            result += chr((ord(char) - shift + key) % 26 + shift)
        else:
            result += char
    return result

def caesar_decipher(text, key):
    return caesar_cipher(text, -key)

def calculate_hash(text):
    return hashlib.sha256(text.encode()).hexdigest()

def main():
    # Step 1: Load cipher text and hash code
    with open('cipher.txt', 'r') as cipher_file:
        cipher_text = cipher_file.read()
        cipher_lines = cipher_text.split('\n')
        hash_code = cipher_lines[-1]
        cipher_text = '\n'.join(cipher_lines[:-1])

    # Step 2: Recompute hash from cipher text
    computed_hash = calculate_hash(cipher_text)

    # Step 3: Compare hashes
    if computed_hash == hash_code:
        print("Hash code matched successfully.")
        # Step 4: Decrypt cipher text
        key = int(open('KEY.TXT', 'r').read())
        plaintext = caesar_decipher(cipher_text, key)
        print("Decrypted plaintext:", plaintext)
    else:
        print("Hash code mismatch.")

if __name__ == "__main__":
    main()

