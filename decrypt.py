from Cryptodome.PublicKey import RSA
from Cryptodome.Cipher import AES, PKCS1_OAEP
import rename

def Descrypt(filename, keypath):
    code = 'nooneknows'
    with open(filename, 'rb') as fobj:
        # 載入私鑰
        private_key = RSA.import_key(open(keypath).read(), passphrase=code)
        enc_session_key, nonce, tag, ciphertext = [ fobj.read(x) 
                                                    for x in (private_key.size_in_bytes(), 
                                                    16, 16, -1) ]
        cipher_rsa = PKCS1_OAEP.new(private_key)
        session_key = cipher_rsa.decrypt(enc_session_key)
        cipher_aes = AES.new(session_key, AES.MODE_EAX, nonce)
        # 解密
        data = cipher_aes.decrypt_and_verify(ciphertext, tag)
    
    with open(filename, 'wb') as wobj:
        wobj.write(data)
    rename.ReserveFilename(filename)
if __name__ == "__main__":
    cyfile=input("欲解密檔案:")
    keypath=input("私鑰路徑:")
    Descrypt(cyfile, keypath)