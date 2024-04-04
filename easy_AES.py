from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import hashlib

def is_pkcs7_padded(message):
    padding = message[-message[-1]:]
    return all(padding[i] == len(padding) for i in range(0, len(padding)))
def decrypt_AES(k: int, ciphertext: str):
    sha1 = hashlib.sha1()
    sha1.update(str(k).encode('ascii'))
    key = sha1.digest()[:16]
    ciphertext = bytes.fromhex(ciphertext)
    cipher = AES.new(key, AES.MODE_ECB)
    plaintext = cipher.decrypt(ciphertext)

    if is_pkcs7_padded(plaintext):
        return unpad(plaintext, 16).decode('ascii')
    else:
        return plaintext.decode('ascii')

cipher = "015e82358048a74b6b441e1dcc781975b73fb14469d5785b148207b596cd6de3"

k = 1891236547812
AES_key = 0

for i in range(1, k+1): # it takes forever :(
    AES_key += i**2


text = decrypt_AES(AES_key, cipher)
print(text) # FLAG{XXXXXXXXXXXXXXXXXXX}
