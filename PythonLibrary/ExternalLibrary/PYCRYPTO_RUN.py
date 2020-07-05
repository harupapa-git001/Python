import base64

from Crypto import Random

from Crypto.Cipher import AES

#暗号化キー
class AESCipher(object):
    def __init__(self, key, block_size = 32):
        self.bs = block_size
        if len(key) >= len(str(block_size)):
            self.key = key[:block_size]
        else:
            self.key = self._pad(key)

    #暗号化オブジェクトの取得
    def encrypt(self, raw):
        raw = self._pad(raw)
        iv = Random.new().read(AES.block_size)
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        return base64.b64encode(iv + cipher.encrypt(raw))
        
    #テキストの暗号化

    def decrypt(self, enc):
        enc = base64.b64decode(enc)
        iv = enc[:AES.block_size]
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        return self._unpad(cipher.decrypt(enc[AES.block_size:]))
    
    def _pad(self, s):
        return s + (self.bs - len(s) % self.bs) * chr(self.bs - len(s) % self.bs)
        
    def _unpad(self, s):
        return s[: -ord(s[len(s) - 1:])]

cipher = AESCipher("VMdcMK1okORuhICPr3qyUYDzWUfTH3bgXwGDEsmqtQLZu4kFCs")

#暗号化

password = cipher.encrypt("hogefuga")

print(password)

#復号化

print(cipher.decrypt(password))
