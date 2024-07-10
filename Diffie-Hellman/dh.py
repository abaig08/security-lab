import random

# Function to perform modular exponentiation


def modular_exponentiation(base, exp, mod):
    result = 1
    base = base % mod
    while exp > 0:
        if (exp % 2) == 1:
            result = (result * base) % mod
        exp = exp >> 1
        base = (base * base) % mod
    return result

# Function to generate private key


def generate_private_key(mod):
    return random.randint(2, mod - 2)

# Function to generate public key


def generate_public_key(base, private_key, mod):
    return modular_exponentiation(base, private_key, mod)

# Function to generate shared secret key


def generate_shared_secret(public_key, private_key, mod):
    return modular_exponentiation(public_key, private_key, mod)

# Diffie-Hellman Key Exchange


def diffie_hellman_key_exchange(base, mod):
    # Both parties generate their private keys
    private_key_A = generate_private_key(mod)
    private_key_B = generate_private_key(mod)

    # Both parties generate their public keys
    public_key_A = generate_public_key(base, private_key_A, mod)
    public_key_B = generate_public_key(base, private_key_B, mod)

    # Both parties generate the shared secret key
    shared_secret_A = generate_shared_secret(public_key_B, private_key_A, mod)
    shared_secret_B = generate_shared_secret(public_key_A, private_key_B, mod)

    return private_key_A, public_key_A, private_key_B, public_key_B, shared_secret_A, shared_secret_B


# Taking input from the user
base = int(input("Enter the base (generator): "))
mod = int(input("Enter the modulus (prime number): "))

# Perform Diffie-Hellman Key Exchange
private_key_A, public_key_A, private_key_B, public_key_B, shared_secret_A, shared_secret_B = diffie_hellman_key_exchange(
    base, mod)

# Display results
print(f"Private Key A: {private_key_A}")
print(f"Public Key A: {public_key_A}")
print(f"Private Key B: {private_key_B}")
print(f"Public Key B: {public_key_B}")
print(f"Shared Secret Key A: {shared_secret_A}")
print(f"Shared Secret Key B: {shared_secret_B}")

# Verify that the shared secret keys match
assert shared_secret_A == shared_secret_B, "Shared secret keys do not match!"
print("Shared secret keys match!")
