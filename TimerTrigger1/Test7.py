path="Test3.txt"

replyX="こんばんは"
reply1=""

while True:
    #リプライを検索する処理を追加

    

    if replyX != reply1:
        reply1=replyX

        with open(path,mode="a") as f:
            f.write(reply1+"\n")

        #一定時間ごとにツイートする処理を追加し、その処理が終わったらcontinueする

    else:
        continue


with open(path) as f:
    s=f.read()
    print(s)

"""
with open(path,mode="a") as f:
    f.write("I like sushi very much.")
    f.write(" ")
"""