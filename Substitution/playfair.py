def generate_playfair_matrix(key):
    key = ''.join(sorted(set(key), key=lambda x: key.index(x)))
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
    matrix = ""
    for char in key:
        if char in alphabet:
            matrix += char
            alphabet = alphabet.replace(char, '')
    matrix += alphabet
    return [matrix[i:i+5] for i in range(0, 25, 5)]


def find_position(matrix, char):
    for i, row in enumerate(matrix):
        for j, letter in enumerate(row):
            if letter == char:
                return i, j


def playfair_encrypt(text, key):
    matrix = generate_playfair_matrix(key)
    text = text.upper().replace('J', 'I')
    text = ''.join([text[i] + ('X' if text[i] == text[i + 1] else '')
                   for i in range(0, len(text) - 1, 2)]) + ('X' if len(text) % 2 != 0 else '')
    encrypted_text = ""
    for i in range(0, len(text), 2):
        row1, col1 = find_position(matrix, text[i])
        row2, col2 = find_position(matrix, text[i + 1])
        if row1 == row2:
            encrypted_text += matrix[row1][(col1 + 1) %
                                           5] + matrix[row2][(col2 + 1) % 5]
        elif col1 == col2:
            encrypted_text += matrix[(row1 + 1) %
                                     5][col1] + matrix[(row2 + 1) % 5][col2]
        else:
            encrypted_text += matrix[row1][col2] + matrix[row2][col1]
    return encrypted_text


def playfair_decrypt(text, key):
    matrix = generate_playfair_matrix(key)
    decrypted_text = ""
    for i in range(0, len(text), 2):
        row1, col1 = find_position(matrix, text[i])
        row2, col2 = find_position(matrix, text[i + 1])
        if row1 == row2:
            decrypted_text += matrix[row1][(col1 - 1) %
                                           5] + matrix[row2][(col2 - 1) % 5]
        elif col1 == col2:
            decrypted_text += matrix[(row1 - 1) %
                                     5][col1] + matrix[(row2 - 1) % 5][col2]
        else:
            decrypted_text += matrix[row1][col2] + matrix[row2][col1]
    return decrypted_text


# Taking input from the user
text = input("Enter text for Playfair Cipher: ").upper().replace(
    ' ', '').replace('J', 'I')
key = input("Enter key for Playfair Cipher: ").upper().replace(' ', '')

encrypted_text = playfair_encrypt(text, key)
decrypted_text = playfair_decrypt(encrypted_text, key)

print(f"Encrypted Text: {encrypted_text}")
print(f"Decrypted Text: {decrypted_text}")
