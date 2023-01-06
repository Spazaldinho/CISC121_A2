"""CISC-121 2022F
Name: Zain Parihar
Student Number: 10219553
Email: 21zp16@queensu.ca
Date: 2022-10-05
I confirm that this assignment solution is my own work and
conforms to Queen's standards of Academic Integrity
"""
from logging import exception
from math import floor

def main():
    """This function is the main program body.
    """
    numbers_inputted = False
    while not numbers_inputted:
        try:
            input_1 = int(input("\n\nPlease input the smaller number: "))
            input_2 = int(input("Please input the larger number: "))
            if input_2 < input_1:
                raise Exception("The first number should be the smaller number.")
            else:
                numbers_inputted = True
        except ValueError:
            print("Please input integers only")
        except Exception: 
            print("Please input the smaller number first.")

    print("\n-------Input-------\n")
    print(f"input one, smaller value: {input_1}")
    print(f"input two, larger value:  {input_2}")
    print("\n-------Output-------\n")

    if input_1 > 20 or input_2 < -20:
        print("Both numbers are invalid\n")
    elif input_1 < -20:
        print(f"First number ({input_1}) is invalid\n")
    elif input_2 > 20:
        print(f"Second number ({input_2}) is invalid\n")
    else:
        print("Both numbers are valid\n")

    difference = abs(input_2 - input_1) 
    cycles = floor((difference - 1) / 5) + 1

    for i in range(1, cycles):
        print(str(input_1 + i*5))

main()
run_again = True
while run_again:
    try:
        user_choice = int(input("\nWould you like to run the program again?\n1. Yes\n2. No\n"))
        if user_choice == 1:
            print("\nRunning again...")
            main()
        elif user_choice == 2:
            print("\nProgram Terminated.")
            run_again = False
        else:
            raise Exception()
    except:
        print("\nPlease input either 1 or 2")
