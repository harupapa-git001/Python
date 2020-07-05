import os
 
path = "/A/B/C/file.py"
 
print("split(): " + str(os.path.split(path)))
 
print("split() ディレクトリ名: " + str(os.path.split(path)[0]))
 
print("split() ファイル名: " + str(os.path.split(path)[1]))
 
print("splitext(): " + str(os.path.splitext(path)))
 
print("splitext() 拡張子より前: " + str(os.path.splitext(path)[0]))
 
print("splitext() 拡張子: " + str(os.path.splitext(path)[1]))
 
path = "/A/B/C"
 
file = "file.py"
 
print("join(): " + os.path.join(path, file))
