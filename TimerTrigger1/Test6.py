#任意のアカウントのツイートに対するリプライを表示
import json
import time
from requests_oauthlib import OAuth1Session
import MeCab
import markovify

CONSUMER_KEY='QV4qhj53ZaSB8sOJtlJ6YcjMR'
CONSUMER_SECRET='2J4TJfDeMe4zhNvgEClQuPoZE7xNb22xvNTJQV8oDWtDcFve1l'
ACCESS_TOKEN='1296742968963956736-teNsz2UkbrNLhSeKahwyO9BgoiGhSL'
ACCESS_TOKEN_SECRET='LEkNSCNCkShxTOM2V5hZ3yYIamhxvtfXBxjRfZNpMukcm'

twitter=OAuth1Session(CONSUMER_KEY,CONSUMER_SECRET,ACCESS_TOKEN,ACCESS_TOKEN_SECRET)

path="Test4.txt"
screenName=""
#markovifyがエラーを吐く文字のリスト
brokenStrings=["(",")","[","]","'",'"']

#スクリーンネームを取得する関数
def getScreenName():
    global screenName, twitter
    timelineUrl="https://api.twitter.com/1.1/statuses/user_timeline.json"
    userId=2377035565 #橋本環奈のユーザーID

    timelineParams={
        "count":1,
        "user_id":userId
    }

    res=twitter.get(timelineUrl,params=timelineParams)

    timelines=json.loads(res.text)
    timeline=timelines[0]

    screenName=timeline["user"]["screen_name"]

getScreenName()



#markovifyのモデルを作成しツイートする
def makeModelAndTweet():
    global path
    with open(path) as file:
        text=file.read()
    tagger=MeCab.Tagger("-Owakati")
    titiedText=tagger.parse(text)

    model=markovify.NewlineText(titiedText, state_size=2)

    #100回モデルを作ってそれでもNoneだったら諦める
    for t in range(100):
        sentence=model.make_short_sentence(200)

        if sentence!=None:
            #空白を消す
            sentence=sentence.replace(" ","")

            #APIを使ってtweetする処理を追加
            print("文が生成されました")
            return sentence

    if sentence==None:
        print("文が生成されませんでした")
        sentence="marcovifyで文が生成されませんでした"
        return sentence



#ツイートする関数
def tweet(tweetSentence):
    global twitter
    url="https://api.twitter.com/1.1/statuses/update.json"
    params={'status':tweetSentence}

    print(tweetSentence)
    print("ツイートします")
    res=twitter.post(url,params=params)
    print(res.status_code)


#リプライを取得
def getAndWriteReply():
    global brokenStrings, path
    searchUrl="https://api.twitter.com/1.1/search/tweets.json"
    counts=0

    searchParams={
        "q":"@"+screenName,
        "count":10,
        "result_type":"recent",
        "lang":"ja",
        "exclude":"retweets"
    }

    #5分ごとに10件リプライを取得し分別する 30分を一区切りとすることを忘れない！
    replyList2=["","","","","","","","","",""]

    while True:
        res=twitter.get(searchUrl,params=searchParams)

        timeline=json.loads(res.text)

        replyList1=[]
        #replyList1に取得した10件を代入する
        for i in range(10):
            information1=timeline["statuses"][i]['in_reply_to_status_id']
            information2=timeline["statuses"][i]['text']

            #本人に直接宛てたリプライか検証し、そうならreplyList1に要素を追加する
            if information1!=None and information2.find("@"+screenName)==0:
                reply=timeline["statuses"][i]["text"]
                #url(画像と動画)と\n(改行記号)、メンションを消去する
                place=reply.find("http")
                if place!=-1:
                    reply=reply[:place]
                reply=reply.replace("\n","")
                reply=reply.replace("@"+screenName+" ","")

                replyList1.append(reply)

        #1度につき10件取得してるからその10件それぞれに対して分別する
        i=0
        for reply1 in replyList1:
            #replyList2の中にreplyList1と一致している要素があればこれが実行
            if reply1==replyList2[0]:
                break
            i+=1
            #iの値がreplyList1の要素の位置と同期されてる

        #replyList2の中にreplyList1と一致している要素がない場合
        if i>len(replyList1)-1:
            #markovifyがエラーを吐く文字を消去する
            for x in range(len(replyList1)-1):
                for brokenString in brokenStrings:
                    replyList1[x]=replyList1[x].replace(brokenString,"")

            replyList2=replyList1
        #replyList2の中にreplyList1と一致している要素がある場合
        else:
            replyList2=[]
            for n in range(i):
                #markovifyがエラーを吐く文字を消去する
                for brokenString in brokenStrings:
                    replyList1[n]=replyList1[n].replace(brokenString,"")
                    replyList2.append(replyList1[n])

        
        print("replyList1を出力します")
        print(replyList1)
        print("------")
        print("replyList2を出力します")
        print(replyList2)
        print("--------")
        

        #replyList2をtextファイルに書き込むコードを作成
        #textをリストとして読み込む
        with open(path) as f:
            text=f.readlines()

        ##replyList2の値をtextファイルから読み込んだリストに入れていく
        for y in range(len(replyList2)):
            text.insert(y,replyList2[y]+"\n")

        #リストをtextに書き込む
        with open(path, mode="w") as f:
            f.writelines(text)

        tweet(makeModelAndTweet())

        #5回目でこのループを抜ける
        counts+=1
        if counts>=5:
            break

        #5分処理を止める
        time.sleep(300)

getAndWriteReply()




