import nltk
import markovify

path="Test.txt"

#markovifyがエラーを吐く文字のリスト
brokenStrings=["(",")","[","]","'",'"']

with open(path) as file:
    morph = nltk.word_tokenize(file.read())

incompleteSentence=" ".join(morph)

#markovifyがエラーを吐く文字を消去する
for brokenStrig in brokenStrings:
    incompleteSentence=incompleteSentence.replace(brokenStrig,"")

print(incompleteSentence)
print("---------")

#".", "!", "?"の場所で改行する
def newLineFuncion():
    global incompleteSentence
    lastStrings=[".","!","?"]

    for lastString in lastStrings:
        incompleteSentence=incompleteSentence.replace(lastString,lastString+"\n")

#マルコフ連鎖のモデルを生成
def marcovFunction():
    model=markovify.NewlineText(incompleteSentence, state_size=2)

    #出力する分の最大文字数
    AmoutOfStrins=200

    sentence=model.make_short_sentence(AmoutOfStrins)

    #semtenceがNoneじゃなくなるまで文を作り続ける
    while sentence==None:
        sentence=model.make_short_sentence(AmoutOfStrins)

    print(sentence)

newLineFuncion()

marcovFunction()
