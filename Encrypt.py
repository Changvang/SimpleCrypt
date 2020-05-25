from cryptography.fernet import Fernet
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import utils,padding
import Load_pem
from pathlib import Path

def Encrypt_File(Fernet_key_file, input_direct, public_key_pem, private_key_pem_with_password):
    try:
        Path('./encrypted').mkdir(parents=True,exist_ok=True)
        #Fernet_key_file = "key.key"
        file = open(Fernet_key_file , 'rb')
        key = file.read()
        file.close()

        intput_file = input_direct.split("/")[-1]
        ouput_file = './encrypted/' + "(encrypted)" + intput_file

        with open( input_direct ,"rb") as f:
            data = f.read()
        #Fernet_encrypt
        fernet = Fernet(key)
        encrypted_data = fernet.encrypt(data)

        #Strip Data
        strip_chars = b"***"

        # Encrypt_key

        public_key = Load_pem.getPublickey(public_key_pem)

        encrypted_key = public_key.encrypt(
            key,
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        )

        # Signature
        private_key = Load_pem.getPrivateKey(private_key_pem_with_password[0], private_key_pem_with_password[1])
        signature = Load_pem.CreateSignature(private_key,input_direct)

        #encrypted
        encrypted = strip_chars + encrypted_key + strip_chars + signature + strip_chars + encrypted_data

        with open(ouput_file, 'wb') as f:
            f.write(encrypted)
        return "Successfull Encrypted, Output file: " + ouput_file
    except Exception as e:
        return "Error when Encrypt, Message: " + e
