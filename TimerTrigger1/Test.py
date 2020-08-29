path="Test.txt"

#文を追加するコード

with open(path,mode="a") as file:
    file.write("I like sushi very much.")
    file.write(" ")

with open(path) as file:
    print(file.read())