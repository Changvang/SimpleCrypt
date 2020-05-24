from cryptography.fernet import Fernet

def generate_new_Fernet_key():
    key = Fernet.generate_key()

    file = open("key.key", 'wb')
    file.write(key)
    file.close()

