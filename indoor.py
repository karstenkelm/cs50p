def convert_to_lowercase(input_string):
    lowercase_string = input_string.lower()
    return lowercase_string

# Take user input
user_input = input("Enter a string in all caps: ")

# Convert to lowercase using the function
result = convert_to_lowercase(user_input)

# Display the result
print("Input in lowercase:", result)