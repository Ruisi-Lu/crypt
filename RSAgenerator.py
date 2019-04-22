from Cryptodome.PublicKey import RSA
def CreateRSAKeys():
    secret = 'nooneknows'
    key = RSA.generate(2048)
    encrypted_key = key.exportKey(passphrase=secret, pkcs=8, protection="scryptAndAES128-CBC")
    # private key
    with open('privateRSA.bin', 'wb') as f:
        f.write(encrypted_key)
    # public key
    with open('publicRSA.pem', 'wb') as f:
        f.write(key.publickey().exportKey())

if __name__ == '__main__':
    CreateRSAKeys()