#".", "!", "?"の場所で改行するコード

path="Test.txt"
path2="Test2.txt"

lastStrings=[".","!","?"]

with open(path) as f:
    s=f.read()

for lastString in lastStrings:
    s=s.replace(lastString,lastString+"\n")

print(s)

with open(path2,mode="a") as file:
    file.write(s)
