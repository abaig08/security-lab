def create_matrix(text, key):
    col = len(key)
    row = len(text) // col
    if len(text) % col != 0:
        row += 1

    matrix = [['' for _ in range(col)] for _ in range(row)]

    k = 0
    for i in range(row):
        for j in range(col):
            if k < len(text):
                matrix[i][j] = text[k]
                k += 1

    return matrix


def row_col_encrypt(text, key):
    col = len(key)
    matrix = create_matrix(text, key)

    sorted_key = sorted(key)
    key_map = {sorted_key[i]: i for i in range(len(key))}

    encrypted_text = ''
    for i in range(col):
        col_index = key_map[key[i]]
        for row in matrix:
            if col_index < len(row):
                encrypted_text += row[col_index]

    return encrypted_text


def row_col_decrypt(cipher, key):
    col = len(key)
    row = len(cipher) // col
    if len(cipher) % col != 0:
        row += 1

    sorted_key = sorted(key)
    key_map = {sorted_key[i]: i for i in range(len(key))}

    matrix = [['' for _ in range(col)] for _ in range(row)]

    k = 0
    for i in range(col):
        col_index = key_map[key[i]]
        for j in range(row):
            if k < len(cipher):
                matrix[j][col_index] = cipher[k]
                k += 1

    decrypted_text = ''
    for row in matrix:
        decrypted_text += ''.join(row)

    return decrypted_text


# Taking input from the user
text = input("Enter text for Row & Column Transformation Cipher: ")
key = input("Enter key for Row & Column Transformation Cipher: ")

encrypted_text = row_col_encrypt(text, key)
decrypted_text = row_col_decrypt(encrypted_text, key)

print(f"Encrypted Text: {encrypted_text}")
print(f"Decrypted Text: {decrypted_text}")
