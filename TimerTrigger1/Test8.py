import json
from requests_oauthlib import OAuth1Session

CONSUMER_KEY='QV4qhj53ZaSB8sOJtlJ6YcjMR'
CONSUMER_SECRET='2J4TJfDeMe4zhNvgEClQuPoZE7xNb22xvNTJQV8oDWtDcFve1l'
ACCESS_TOKEN='1296742968963956736-teNsz2UkbrNLhSeKahwyO9BgoiGhSL'
ACCESS_TOKEN_SECRET='LEkNSCNCkShxTOM2V5hZ3yYIamhxvtfXBxjRfZNpMukcm'

twitter=OAuth1Session(CONSUMER_KEY,CONSUMER_SECRET,ACCESS_TOKEN,ACCESS_TOKEN_SECRET)

url='https://api.twitter.com/1.1/statuses/user_timeline.json'

params={'count':2} #取得するタイムラインの数を指定

res=twitter.get(url,params=params)

print(res.status_code)

timelines=json.loads(res.text)

for timeline in timelines:
    information1=timeline['in_reply_to_status_id']
    information2=timeline['text']

    if information1!=None:
        print("information1はNoneではありません")
    
    if information2.find('@H_KANNA_0203')==0:
        print("橋本環奈へ直接宛てたツイートです")

    if information1!=None and information2.find('@H_KANNA_0203')==0:
        print("橋本環奈へ直接宛てたリプライです")

    print("--------")


replyList1=[]
replyList1.append(None)
replyList1.append("こんにちは")

print(replyList1)
