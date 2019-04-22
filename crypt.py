from Cryptodome.PublicKey import RSA
from Cryptodome.Random import get_random_bytes
from Cryptodome.Cipher import AES, PKCS1_OAEP
import rename

def Encrypt(filename, publicKeyPath):         
    data = ''
    with open(filename, 'rb') as f:
        data = f.read()
    with open(filename, 'wb') as out_file:
        #載入公鑰
        recipient_key = RSA.import_key(open(publicKeyPath).read())
        #產生16字元AES key
        session_key = get_random_bytes(16)
        # Encrypt the session key with the public RSA key
        cipher_rsa = PKCS1_OAEP.new(recipient_key)
        out_file.write(cipher_rsa.encrypt(session_key))
        # Encrypt the data with the AES session key
        cipher_aes = AES.new(session_key, AES.MODE_EAX)
        ciphertext, tag = cipher_aes.encrypt_and_digest(data)
        out_file.write(cipher_aes.nonce)
        out_file.write(tag)
        out_file.write(ciphertext)
    rename.RenameFile(filename)

if __name__ == "__main__":
    cyfile=input("欲加密檔案:")
    keypath=input("公鑰路徑:")
    Encrypt(cyfile, keypath)