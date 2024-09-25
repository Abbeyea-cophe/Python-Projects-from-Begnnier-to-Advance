def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def mod_inverse(a, m):
    m0, x0, x1 = m, 0, 1
    while a > 1:
        q = a // m
        m, a = a % m, m
        x0, x1 = x1 - q * x0, x0
    return x1 + m0 if x1 < 0 else x1

def generate_keypair(p, q):
    n = p * q
    phi = (p - 1) * (q - 1)
    e = 2
    while gcd(e, phi) != 1:
        e += 1
    d = mod_inverse(e, phi)
    return ((e, n), (d, n))

def encrypt(public_key, plaintext):
    e, n = public_key
    return [pow(ord(char), e, n) for char in plaintext]

def decrypt(private_key, ciphertext):
    d, n = private_key
    return ''.join([chr(pow(char, d, n)) for char in ciphertext])

if __name__ == "__main__":
    p = int(input("Enter the first prime number (p): "))
    q = int(input("Enter the second prime number (q): "))
    message = input("Enter the message to be encrypted: ")

    public_key, private_key = generate_keypair(p, q)
    print("Public Key (e, n):", public_key)
    print("Private Key (d, n):", private_key)

    encrypted_message = encrypt(public_key, message)
    print("Encrypted message:", encrypted_message)

    decrypted_message = decrypt(private_key, encrypted_message)
    print("Decrypted message:", decrypted_message)
