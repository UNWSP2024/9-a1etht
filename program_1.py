#Programmer: Alethea Lo
#Date: 3/24/25
#Title: Item Counter

with open("names.txt", "r") as file:
    r"C:\Users\aleth\Documents\names.txt"

    name_count = sum(1 for line in file)

print(f"Total number of names in the file: {name_count}")