import json
import re
from requests_oauthlib import OAuth1Session

texts=[]

def collectTweets():
    CONSUMER_KEY='QV4qhj53ZaSB8sOJtlJ6YcjMR'
    CONSUMER_SECRET='2J4TJfDeMe4zhNvgEClQuPoZE7xNb22xvNTJQV8oDWtDcFve1l'
    ACCESS_TOKEN='1296742968963956736-teNsz2UkbrNLhSeKahwyO9BgoiGhSL'
    ACCESS_TOKEN_SECRET='LEkNSCNCkShxTOM2V5hZ3yYIamhxvtfXBxjRfZNpMukcm'

    twitter=OAuth1Session(CONSUMER_KEY,CONSUMER_SECRET,ACCESS_TOKEN,ACCESS_TOKEN_SECRET)

    url='https://api.twitter.com/1.1/statuses/user_timeline.json'

    params={'count':50,
            'screen_name':'realDonaldTrump',
            'include_rts': 'false',
            }

    res=twitter.get(url,params=params)

    print(res.status_code)

    timelines=json.loads(res.text)

    for i in range(len(timelines)):
        timeline=timelines[i]
        tweet=timeline['text']

        #URLを消去する
        num1=tweet.find("http")
        renewedTweet1=tweet[:num1]

        #ピリオド3連続やピリオド3つが1文字になった文字列を削除する
        renewedTweet2=renewedTweet1.replace("…","")
        perfectRenewedTweet=renewedTweet2.replace("...","")

        #トランプのツイートをリストにいれる
        if perfectRenewedTweet:
                texts.append(perfectRenewedTweet)

    
    print(texts) 

collectTweets()

#2ページに渡ってツイートをしたときの'...'の文字列を消去するコードを追加する