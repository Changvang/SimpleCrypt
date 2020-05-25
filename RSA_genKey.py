from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization
from pathlib import Path

def generate_key(password):
    #create a folder keys if not exit
    Path('./keys').mkdir(parents=True,exist_ok=True)
    try:
        # Create private key
        private_key = rsa.generate_private_key(
            public_exponent=65537,
            key_size=4096,
            backend=default_backend()
        )

        # Create private key pem with password
        private_pem = private_key.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.PKCS8,
            encryption_algorithm=serialization.BestAvailableEncryption(str.encode(password))
        )

        private_key_file = open( "keys/private_key.pem",'wb')
        private_key_file.write(private_pem)
        private_key_file.close()

        #Create public key
        public_pem = private_key.public_key().public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo
        )

        public_key_file = open("keys/public_key.pem",'wb')
        public_key_file.write(public_pem)
        public_key_file.close()

        return 1
    except:
        return 0

# if __name__ == "__main__":
#     generate_key("", "ILOVEYOU")
