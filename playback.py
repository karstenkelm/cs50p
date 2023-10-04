def slowmo(sentence):
    words = sentence.split()
    result = "...".join(words)
    print(result)

input = input("write something: ")

slowmo(input)