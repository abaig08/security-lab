import numpy as np


def hill_encrypt(text, key):
    text = text.replace(" ", "")
    n = int(np.sqrt(len(key)))
    key_matrix = np.array([ord(char) - ord('A') for char in key]).reshape(n, n)
    text_vector = [ord(char) - ord('A') for char in text]

    while len(text_vector) % n != 0:
        text_vector.append(ord('X') - ord('A'))

    text_matrix = np.array(text_vector).reshape(-1, n)
    encrypted_matrix = (text_matrix @ key_matrix) % 26
    encrypted_text = ''.join(chr(num + ord('A'))
                             for num in encrypted_matrix.flatten())

    return encrypted_text


def hill_decrypt(text, key):
    n = int(np.sqrt(len(key)))
    key_matrix = np.array([ord(char) - ord('A') for char in key]).reshape(n, n)
    inverse_key_matrix = np.linalg.inv(key_matrix).astype(float)
    inverse_key_matrix = np.round(
        inverse_key_matrix * np.linalg.det(key_matrix)).astype(int) % 26
    inverse_key_matrix = (inverse_key_matrix *
                          pow(int(np.linalg.det(key_matrix)), -1, 26)) % 26
    text_vector = [ord(char) - ord('A') for char in text]
    text_matrix = np.array(text_vector).reshape(-1, n)
    decrypted_matrix = (text_matrix @ inverse_key_matrix) % 26
    decrypted_text = ''.join(chr(num + ord('A'))
                             for num in decrypted_matrix.flatten())

    return decrypted_text


# Taking input from the user
text = input("Enter text for Hill Cipher: ").upper().replace(' ', '')
key = input("Enter key for Hill Cipher (must be a perfect square length): ").upper(
).replace(' ', '')

encrypted_text = hill_encrypt(text, key)
decrypted_text = hill_decrypt(encrypted_text, key)

print(f"Encrypted Text: {encrypted_text}")
print(f"Decrypted Text: {decrypted_text}")
