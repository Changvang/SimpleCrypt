from cryptography.fernet import Fernet
from cryptography.fernet import Fernet
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import utils,padding
import Load_pem
from pathlib import Path

def Decrypt_File(input_direct, public_key_pem, private_key_pem_with_password ):
    try:
        Path('./decrypted').mkdir(parents=True,exist_ok=True)
        intput_file = input_direct.split("/")[-1]
        ouput_file = "./decrypted/" + "(decrypted)" + intput_file.replace("(encrypted)","")

        #Strip Data
        strip_chars = b"***"

        #Encrypted
        with open( input_direct ,"rb") as f:
            encrypted = f.read()

        #Split_encrypted
        (Nothings, encrypted_key, signature, encrypted_data) = encrypted.split(strip_chars)

        # Decrypt_key
        private_key = Load_pem.getPrivateKey(private_key_pem_with_password[0], private_key_pem_with_password[1])
        decrypted_key = private_key.decrypt(
            encrypted_key,
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        )

        # decrypt file
        fernet = Fernet(decrypted_key)
        decrypted = fernet.decrypt(encrypted_data)

        with open(ouput_file, 'wb') as f:
            f.write(decrypted)
        print("Successfull Decrypted")

        # Check_Signature
        public_key = Load_pem.getPublickey(public_key_pem)
        checkSign = Load_pem.CheckValueSignature(public_key, signature, ouput_file)
        if checkSign:
            print("Integrity")
        else:
            print("Not Intergrity")
    except Exception as e:
        print("Error when Decrypted")
        print("Message: ", e)

    




