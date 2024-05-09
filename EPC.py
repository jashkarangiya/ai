import string
import random

# Define the special symbols
special_symbols = ['@', '#', '$', '%', '*']

# Define the complete character set
characters = list(string.ascii_lowercase) + list(string.digits) + special_symbols

# Helper function to generate the key
def key_generation():
    key = ''.join(random.sample(string.ascii_lowercase, random.randint(6, 8)))
    return key

# Helper function to remove duplicates and create the matrix
def generate_matrix(key, characters):
    matrix = []
    temp_list = key + ''.join(sorted(set(characters) - set(key)))
    for i in range(12):
        matrix.append(list(temp_list[i*12:(i+1)*12]))
    return matrix

# Helper function to process the input text
def processed_input(text):
    processed_text = []
    for char in text.lower():
        if char.isalnum() or char in special_symbols:
            processed_text.append(char)
    processed_text = ''.join(processed_text).replace('j', 'i')
    if len(processed_text) % 2 != 0:
        processed_text += 'x'
    return [processed_text[i:i+2] for i in range(0, len(processed_text), 2)]

# Function to encrypt the text
def encrypt_text(text, matrix, key):
    encrypted_text = []
    for pair in processed_input(text):
        try:
            row1, col1 = divmod(matrix.index(pair[0]), 12)
            row2, col2 = divmod(matrix.index(pair[1]), 12)
            if row1 == row2:
                encrypted_text.append(matrix[row1][(col1+1)%12] + matrix[row1][(col2+1)%12])
            elif col1 == col2:
                encrypted_text.append(matrix[(row1+1)%12][col1] + matrix[(row2+1)%12][col1])
            else:
                encrypted_text.append(matrix[row1][col2] + matrix[row2][col1])
        except ValueError:
            # Handle case where character is not found in matrix
            encrypted_text.append(pair)
    return ''.join(encrypted_text)

# Function to decrypt the text
def decrypt_text(text, matrix, key):
    decrypted_text = []
    for pair in processed_input(text):
        try:
            row1, col1 = divmod(matrix.index(pair[0]), 12)
            row2, col2 = divmod(matrix.index(pair[1]), 12)
            if row1 == row2:
                decrypted_text.append(matrix[row1][(col1-1)%12] + matrix[row1][(col2-1)%12])
            elif col1 == col2:
                decrypted_text.append(matrix[(row1-1)%12][col1] + matrix[(row2-1)%12][col1])
            else:
                decrypted_text.append(matrix[row1][col2] + matrix[row2][col1])
        except ValueError:
            # Handle case where character is not found in matrix
            decrypted_text.append(pair)
    return ''.join(decrypted_text)

# Main function
def main():
    # Generate the key
    key = key_generation()
    print(f"Key: {key}")

    # Generate the matrix
    matrix = generate_matrix(key, characters)
    print("Matrix:")
    for row in matrix:
        print(' '.join(row))

    # Get the input text from the file
    with open('PT.txt', 'r') as file:
        plaintext = file.read()

    print(f"\nPlaintext: {plaintext}")

    # Encrypt the text
    ciphertext = encrypt_text(plaintext, matrix, key)
    print(f"Ciphertext: {ciphertext}")

    # Decrypt the text
    decrypted_text = decrypt_text(ciphertext, matrix, key)
    print(f"Decrypted text: {decrypted_text}")

    # Write the cipher-text and plain-text pairs to the output file
    with open('OUTPUT.txt', 'w') as file:
        file.write(f"Plaintext: {plaintext}\nCiphertext: {ciphertext}")

if __name__ == "__main__":
    main()

