#任意のアカウントのツイートに対するリプライを表示
import json
import time
from requests_oauthlib import OAuth1Session

CONSUMER_KEY='QV4qhj53ZaSB8sOJtlJ6YcjMR'
CONSUMER_SECRET='2J4TJfDeMe4zhNvgEClQuPoZE7xNb22xvNTJQV8oDWtDcFve1l'
ACCESS_TOKEN='1296742968963956736-teNsz2UkbrNLhSeKahwyO9BgoiGhSL'
ACCESS_TOKEN_SECRET='LEkNSCNCkShxTOM2V5hZ3yYIamhxvtfXBxjRfZNpMukcm'

twitter=OAuth1Session(CONSUMER_KEY,CONSUMER_SECRET,ACCESS_TOKEN,ACCESS_TOKEN_SECRET)

screenName=""
reply=""

#スクリーンネームを取得する関数
def getScreenName():
    global screenName
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


#リプライを取得
def getReply():
    global reply
    searchUrl="https://api.twitter.com/1.1/search/tweets.json"

    searchParams={
        "q":screenName,
        "count":1,
        "result_type":"recent",
        "lang":"ja",
        "exclude":"retweets"
    }

    res=twitter.get(searchUrl,params=searchParams)

    replies=json.loads(res.text)
    reply=replies["statuses"][0]["text"]

getReply()

print("--------")
print(reply)

"""
一定時間ごとにリプライを取得し、前回取得したリプライと新しいリプライが異なっていれば
そのリプライをテキストファイルに出力する。
"""

path="Test3.txt"


