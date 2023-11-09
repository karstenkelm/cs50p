smiley_mapping = {":)": "😊"}  # You can add more mappings if needed

input_str = input()

for key, value in smiley_mapping.items():
    input_str = input_str.replace(key, value)

print(input_str)
