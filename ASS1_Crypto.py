import Create_key
import RSA_genKey
import Encrypt
import Decrypt
import UI.entry

# You can create new pair RSA (private_key, public_key) and private_key need pass word for authentiacation 
#RSA_genKey("", "Crypto")
#1. First create a key to Fernet algorithm to de/encrypt
#Create_key.generate_new_Fernet_key() 
#2. Create Encrypt_File(Fernetkey, fileNeedEncrypt, publickeyOfReceiver, (privatekeyOfSender, PasswordOfPrivateKey))
#Encrypt.Encrypt_File("key.key", "TestMusic.mp3", './keys/public_key.pem', ('./keys/private_key.pem', 'ILOVEYOU'))
#3. Create Decrypt_File(fileNeedDecrypt, publickeyOfSender, (privatekeyOfReceiver, PasswordOfPrivateKey))
#Decrypt.Decrypt_File("./encrypted/(encrypted)TestMusic.mp3", './keys/public_key.pem', ('./keys/private_key.pem', 'ILOVEYOU'))
#4. Print result

UI.entry.run()