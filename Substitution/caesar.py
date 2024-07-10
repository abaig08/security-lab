def caesar_encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            shift_base = 65 if char.isupper() else 97
            encrypted_text += chr((ord(char) - shift_base +
                                  shift) % 26 + shift_base)
        else:
            encrypted_text += char
    return encrypted_text


def caesar_decrypt(text, shift):
    return caesar_encrypt(text, -shift)


# Taking input from the user
text = input("Enter text for Caesar Cipher: ")
shift = int(input("Enter shift value: "))

encrypted_text = caesar_encrypt(text, shift)
decrypted_text = caesar_decrypt(encrypted_text, shift)

print(f"Encrypted Text: {encrypted_text}")
print(f"Decrypted Text: {decrypted_text}")
