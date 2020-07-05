class UserInfo:
    def __init__(self, name, birth, address):
        print("initialize instance")#コンストラクタで初期化
        
        self.name = None
        self.birth = 0
        self.address = None
'''taro = UserInfo()
#ex1
'''
taro = UserInfo("taro", 1980, "tokyo")

print(taro.name)

print(taro.birth)

print(taro.address)

