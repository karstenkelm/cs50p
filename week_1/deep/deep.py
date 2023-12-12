### deep.py

q = input("What is the Answer to the Great Question of Life, the Universe and Everything? ")

match q:
    case "42" | "forty-two" | "forty two":
        print("YEP!")
    case _:
        print("NOPE")