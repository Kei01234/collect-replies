import re

url="https://kei01234.github.io/Kei.github.io/"

texts=[f"{url} I wanna know the good way to delete URLs which are in a character string.",
f"I wanna know the good way to delete URLs which are in a character string. {url}",
f"{url} I wanna know the good way to delete URLs which are in a character string. {url}"
]

for text in texts:
    num=text.find("http") #httpという文字列が含まれている場所
    print(num)
    print(text[:num])
    print("----------")

