from Crypto.Cipher import DES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes


def des_encrypt(plain_text, key):
    des = DES.new(key, DES.MODE_ECB)
    padded_text = pad(plain_text.encode('utf-8'), DES.block_size)
    encrypted_text = des.encrypt(padded_text)
    return encrypted_text


def des_decrypt(encrypted_text, key):
    des = DES.new(key, DES.MODE_ECB)
    decrypted_text = unpad(des.decrypt(encrypted_text), DES.block_size)
    return decrypted_text.decode('utf-8')


# Taking input from the user
plain_text = input("Enter text to encrypt using DES: ")
key = input("Enter an 8-byte key for DES: ")

if len(key) != 8:
    raise ValueError("Key must be 8 bytes long")

# Encrypting the text
encrypted_text = des_encrypt(plain_text, key.encode('utf-8'))
print(f"Encrypted Text: {encrypted_text.hex()}")

# Decrypting the text
decrypted_text = des_decrypt(encrypted_text, key.encode('utf-8'))
print(f"Decrypted Text: {decrypted_text}")
