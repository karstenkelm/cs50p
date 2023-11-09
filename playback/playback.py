# 1. Without a function
# input = input()

# process = input.split()

# slow = "...".join(process)
# print(slow)

# 2. Within a function

def slowdown(input_string):
    words = input_string.split()
    result = "...".join(words)
    return result

# Example usage:
input_string = input()
result = slowdown(input_string)
print(result)
