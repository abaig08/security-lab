from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes


def aes_encrypt(plain_text, key):
    cipher = AES.new(key, AES.MODE_CBC)
    iv = cipher.iv
    padded_text = pad(plain_text.encode('utf-8'), AES.block_size)
    encrypted_text = cipher.encrypt(padded_text)
    return iv + encrypted_text


def aes_decrypt(encrypted_text, key):
    iv = encrypted_text[:AES.block_size]
    cipher = AES.new(key, AES.MODE_CBC, iv)
    encrypted_text = encrypted_text[AES.block_size:]
    decrypted_text = unpad(cipher.decrypt(encrypted_text), AES.block_size)
    return decrypted_text.decode('utf-8')


# Taking input from the user
plain_text = input("Enter text to encrypt using AES: ")
key = get_random_bytes(16)  # AES-128 key (16 bytes)

# Encrypting the text
encrypted_text = aes_encrypt(plain_text, key)
print(f"Encrypted Text (hex): {encrypted_text.hex()}")

# Decrypting the text
decrypted_text = aes_decrypt(encrypted_text, key)
print(f"Decrypted Text: {decrypted_text}")
