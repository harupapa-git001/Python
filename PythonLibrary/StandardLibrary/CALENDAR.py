'''
    １０．calendar
    
    "calendar"は日付操作を行うためのライブラリです。
    
    いわゆる「カレンダー」に関連する様々な機能を提供します。

'''
#日時情報の表示

import calendar

#月末日の表示

print(calendar.monthrange(2020, 3)[1])

print(calendar.monthrange(2020, 4)[1])

#年月を指定してカレンダーを表示

calendar.prmonth(2020, 3)

#起点を日曜にしたカレンダーを表示

c = calendar.TextCalendar(calendar.SUNDAY)

c.prmonth(2020, 3)

#うるう年かどうか

print(calendar.isleap(2020))

print(calendar.isleap(2021))
