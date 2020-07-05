'''
    ３．pytz
    
    "pytz"はタイムゾーンを扱うためのライブラリです。
    
    本書ではバージョン2017.03を扱います。

    #インストール
    
    ■Windows
    
    pip install pytz
    
    ■macOS
    
    pip3 install pytz

    標準の"datetime"でもタイムゾーンは扱えますが、こちらのライブラリの方が強力な機能を提供します。
    
    以下は現在日時をアラスカのタイムゾーンに変換する例です。

'''
#タイムゾーンの変換

import pytz

from datetime import datetime

now = datetime.now()

print("現在日時:", now)

#東京のタイムゾーンを取得

timezone = pytz.timezone("Asia/Tokyo")

print("東京のタイムゾーン: ", timezone)

#現在日時をタイムゾーン付きに変換

aware_datetime = timezone.localize(now)

print("変換した現在日時: ", aware_datetime)

#言在日jをUTCに変換

utc = pytz.utc

utc_datetime = utc.normalize(aware_datetime.astimezone(utc))

#UTCをアラスカに変換

alaska_timezone = pytz.timezone("US/Alaska")

alaska_datetime =alaska_timezone.normalize(utc_datetime.astimezone(alaska_timezone))

print("現在日時（アラスカ）: ", alaska_datetime)
