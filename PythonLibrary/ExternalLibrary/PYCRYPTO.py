'''
    14. pycrypto
    
    "pycrypto"は様々な暗号アルゴリズムとプロトコルを提供するライブラリです。
    
    本書ではバージョン2.6.1を使用します。
    
    #インストール
    
    ■Windows
    
    pip install pycrypto
    
    ■macOS
    
    pip3 install pycrypto
    
    本書では暗号化アルゴリズムの一つである「AES」を使った使用例を掲載します。
'''
#AESを使った暗号化/復号化

from Crypto.Cipher import AES

#暗号化キー

keywd = "That's a lie!!!"

#暗号化するテキスト

text = "I'm pro-wrestler"

#暗号化オブジェクトの取得

crypto = AES.new(keywd) #エラーなう（原因特定中）

#テキストの暗号化

cipher_text = crypto.encrypt(text)

print(cipher_text)

#テキストの復号化

original_text= crypto.decrypt(cipher_text)

print(original_text.decode("utf-8"))


'''
    [出力結果]
    b'\xae\x1d9khe\xf3VSz\xe0Ig\x9c\xc4a'
    I'm pro-wrestler
    
'''
