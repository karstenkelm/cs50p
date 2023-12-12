###
def main():
    x = int(input("Whats X? "))
    if is_even(x):
        print("X is even")
    else:
        print("Odd")

def is_even(n):
    return n % 2 == 0

main()