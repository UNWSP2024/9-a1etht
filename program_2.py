#Programmer: Alethea Lo
#Date: 3/24/25
#Title: Random Number File Writer

import random
while True:
    try:
        count = int(input("Enter how many random numbers to generate (up to 1000): "))
        if 1 <= count <= 1000:
            break
        else:
            print("Please enter a number between 1 and 1000.")
    except ValueError:
        print("Invalid input. Please enter a valid integer.")


with open("random_numbers.txt", "w") as file:
    for _ in range(count):

        random_number = random.randint(1, 500)

        file.write(f"{random_number}\n")

print(f"{count} random numbers have been written to 'random_numbers.txt'.")