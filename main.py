# main.py
def is_even(number):
    return number % 2 == 0

def find_square(number):
    return number ** 2

def main():
    number = int(input("Enter a number: "))
    #To find given number is even or add
    if is_even(number):
        print(f"{number} is even.")
    else:
        print(f"{number} is odd.")
    #To find the square of given number
    print(f"The square of {number} is {find_square(number)}")
    

if __name__ == "__main__":
    main()
