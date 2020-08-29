#MeCabをインストール
import MeCab

me = MeCab.Tagger ("-Ochasen")
print(me.parse ("あの花は美しい"))