### bank.py

greeting = input("Greeting: ")

match greeting:
    case "Hello" | "hello" | "hellooo":
        print("$0.00")
    case _ if greeting.lower().startswith("h"):
        print("$20.00")
    case _:
        print("$100.00")