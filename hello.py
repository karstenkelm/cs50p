# Ask user for their name
name = input("Whats your name? ").strip().title()

# Split user's name into first and last name
first, last = name.split(" ")

# Say hello to user
print(f"moinsen, {first}")