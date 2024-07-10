def vigenere_encrypt(text, key):
    encrypted_text = ""
    key_length = len(key)
    for i, char in enumerate(text):
        if char.isalpha():
            shift = ord(key[i % key_length].upper()) - ord('A')
            shift_base = 65 if char.isupper() else 97
            encrypted_text += chr((ord(char) - shift_base +
                                  shift) % 26 + shift_base)
        else:
            encrypted_text += char
    return encrypted_text


def vigenere_decrypt(text, key):
    decrypted_text = ""
    key_length = len(key)
    for i, char in enumerate(text):
        if char.isalpha():
            shift = ord(key[i % key_length].upper()) - ord('A')
            shift_base = 65 if char.isupper() else 97
            decrypted_text += chr((ord(char) - shift_base -
                                  shift) % 26 + shift_base)
        else:
            decrypted_text += char
    return decrypted_text


# Taking input from the user
text = input("Enter text for Vigenere Cipher: ")
key = input("Enter key for Vigenere Cipher: ")

encrypted_text = vigenere_encrypt(text, key)
decrypted_text = vigenere_decrypt(encrypted_text, key)

print(f"Encrypted Text: {encrypted_text}")
print(f"Decrypted Text: {decrypted_text}")
