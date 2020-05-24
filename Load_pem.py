from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import utils,padding

def getPrivateKey(privatekey_pem_path, password):
    with open(privatekey_pem_path, "rb") as key_file:
        private_key = serialization.load_pem_private_key(
                key_file.read(),
                password=str.encode(password),
                backend=default_backend()
            )
    return private_key

def CreateSignature(private_key, inputfile_direct):
    #privatekey_pem_path = "./keys/private_key.pem" # Input private key
    #Pre Hash
    chosen_hash = hashes.SHA256()
    hasher = hashes.Hash(chosen_hash, default_backend())
    # Read file
    with open( inputfile_direct ,"rb") as f:
        for byte_block in iter(lambda : f.read(4096), b""):
            hasher.update(byte_block)
    #Update digest
    digest = hasher.finalize()


    signature = private_key.sign(
        digest,
        padding.PSS(
            mgf=padding.MGF1(hashes.SHA256()),
            salt_length=padding.PSS.MAX_LENGTH
        ),
        utils.Prehashed(chosen_hash)
    )
    return signature

def getPublickey(publickey_pem_path):
    with open(publickey_pem_path, "rb") as key_file:
        public_key = serialization.load_pem_public_key(
                key_file.read(),
                backend=default_backend()
            )
    return public_key

def CheckValueSignature(public_key, signature, newinputfile_directs):
    #publickey_pem_path = "./keys/public_key.pem"
    try:
        chosen_hash = hashes.SHA256()
        hasher = hashes.Hash(chosen_hash, default_backend())
        # Read file
        with open( newinputfile_directs ,"rb") as f:
            for byte_block in iter(lambda : f.read(4096), b""):
                hasher.update(byte_block)
        #Update digest
        new_digest = hasher.finalize()
        
        public_key.verify(
            signature,
            new_digest,
            padding.PSS(
                mgf=padding.MGF1(hashes.SHA256()),
                salt_length=padding.PSS.MAX_LENGTH
            ),
            utils.Prehashed(chosen_hash)
        )
        return True
    except:
        return False