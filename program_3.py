#Programmer: Alethea Lo
#Date: 3/24/25
#Title: Average Numbers

def calculate_total():
    try:

        with open("numbers.txt", "r") as file:
            total = 0

            for line in file:
                try:

                    total += int(line.strip())
                except ValueError:
                    print(f"Warning: '{line.strip()}' is not a valid integer and will be skipped.")
            print(f"The total sum of the numbers is: {total}")

    except FileNotFoundError:
        print("Error: The file 'numbers.txt' was not found.")

    except Exception as e:
        print(f"An unexpected error occurred: {e}")

#END OF PROGRAM
calculate_total()