import hashlib
from cryptography.fernet import Fernet

# Function to encrypt message and hash
def encrypt_message_and_hash(message, key):
    # Generate hash of the message
    hash_value = hashlib.sha256(message.encode()).hexdigest()
    # Encrypt message along with hash
    cipher_suite = Fernet(key)
    encrypted_message = cipher_suite.encrypt((message + hash_value).encode())
    return encrypted_message

# Function to decrypt message and extract hash
def decrypt_message_and_extract_hash(encrypted_message, key):
    cipher_suite = Fernet(key)
    decrypted_message = cipher_suite.decrypt(encrypted_message).decode()
    # Extract original message and hash from decrypted message
    message = decrypted_message[:-64]  # Extract original message
    received_hash = decrypted_message[-64:]  # Extract received hash
    return message, received_hash

# Function to verify message integrity
def verify_message_integrity(message, received_hash):
    computed_hash = hashlib.sha256(message.encode()).hexdigest()
    return computed_hash == received_hash

def main():
    # Secret key (for demonstration purposes, this should be securely shared between Bob and Alice)
    key = Fernet.generate_key()

    # Bob prepares the message
    original_message = "Hello Alice, this is a secret message."
    encrypted_bundle = encrypt_message_and_hash(original_message, key)

    # Bob sends the encrypted bundle to Alice
    # In a real scenario, this would involve sending the encrypted bundle over a communication channel

    # Alice receives the encrypted bundle
    # In this simulation, Alice receives the encrypted bundle from Bob
    received_encrypted_bundle = encrypted_bundle

    # Alice decrypts the encrypted bundle and extracts message and hash
    received_message, received_hash = decrypt_message_and_extract_hash(received_encrypted_bundle, key)

    # Alice verifies the integrity of the received message
    if verify_message_integrity(received_message, received_hash):
        print("Message integrity verified. Decrypted Message:", received_message)
    else:
        print("Message integrity verification failed. The message may have been tampered with.")

if __name__ == "__main__":
    main()

