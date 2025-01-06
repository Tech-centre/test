# main.py
def is_even(number):
    return number % 2 == 0

def main():
    number = int(input("Enter a number: "))
    if is_even(number):
        print(f"{number} is even.")
    else:
        print(f"{number} is odd.")

if __name__ == "__main__":
    main()
