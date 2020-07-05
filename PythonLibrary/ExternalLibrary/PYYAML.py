'''
    12. PyYAML
    
    "PyYAML"はPython用のYAMLパーサーです。
    
    本書ではバージョン3.12を扱います。
    
    #インストール
    
    ■Windows
    
    pip install PyYAML
    
    ■macOS
    
    pip3 install PyYAML
    
    このライブラリはYAMLの読み書きが行えます。
'''
#YAMLの書き込み

import yaml

data = {"iPhone": ["Shiro", "Fuka", "Chika"], "Android":["masaru", "satoru"]}

with open("hoge.yaml", "w") as f:
    #YAMLデータの書き込み
    
    f.write(yaml.dump(data))

'''

'''
#YAMLの読み込み

import yaml

with open("hoge.yaml", "r") as f:
    #YAMLデータの読み込み
    
    print(yaml.load(f))

'''
    ※importする際の記述が"yaml"である点に注意しましょう。
'''
