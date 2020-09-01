import MeCab
import markovify

path="Test4.txt"


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

        break


