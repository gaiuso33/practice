from cryptography.fernet import Fernet

key = Fernet.generate_key()
cipher = Fernet(key)

def encrypt_password(password):
    return cipher.encrypt(password.encode()).decode()

def decrypt_password(encrypted_password):
    return cipher.decrypt(encrypted_password.encode()).decode()

password = input("Enter password: ")
encrypted = encrypt_password(password)
print(f"🔐 Encrypted: {encrypted}")
print(f"🔓 Decrypted: {decrypt_password(encrypted)}")
