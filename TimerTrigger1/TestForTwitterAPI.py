import json
import time
from requests_oauthlib import OAuth1Session

CONSUMER_KEY='QV4qhj53ZaSB8sOJtlJ6YcjMR'
CONSUMER_SECRET='2J4TJfDeMe4zhNvgEClQuPoZE7xNb22xvNTJQV8oDWtDcFve1l'
ACCESS_TOKEN='1296742968963956736-teNsz2UkbrNLhSeKahwyO9BgoiGhSL'
ACCESS_TOKEN_SECRET='LEkNSCNCkShxTOM2V5hZ3yYIamhxvtfXBxjRfZNpMukcm'

twitter=OAuth1Session(CONSUMER_KEY,CONSUMER_SECRET,ACCESS_TOKEN,ACCESS_TOKEN_SECRET)

#時刻の表示設定
now = time.ctime()
cnvtime = time.strptime(now)
setTime=time.strftime("%Y/%m/%d %H時%M分%S秒", cnvtime)

url='https://api.twitter.com/1.1/statuses/update.json'
params={'status':setTime+'にTwitterAPIから投稿'}

res=twitter.post(url,params=params)
print(res.status_code)