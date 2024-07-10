import hashlib

# Prompt the user for input
text = input("Enter the text to hash: ")

# Encode the text to bytes
text_bytes = text.encode()

# Create a new SHA-1 hash object
sha1_hash = hashlib.sha1()

# Update the hash object with the bytes of the text
sha1_hash.update(text_bytes)

# Get the hexadecimal representation of the digest
sha1_digest = sha1_hash.hexdigest()

print(f"SHA-1 Digest: {sha1_digest}")
