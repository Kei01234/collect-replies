path="Test4.txt"
l = ['One', 'Two', 'Three']


#textをリストxとして読み込む
with open(path) as f:
    x=f.readlines()

#リストlの値をtextファイルから読み込んだリストxに入れていく
for y in range(len(l)):
    x.insert(y,l[y]+"\n")

#リストをtextに書き込む
with open(path, mode="w") as f:
    f.writelines(x)

#text読み込み
with open(path) as f:
    print(f.read())


"""
for text in l:
    print(text) #textに入ってる\nは適用される
"""