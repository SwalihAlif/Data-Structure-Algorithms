
import os

os.rename("examplessssss.txt", "example.txt")

with open("example.txt", "r") as file:
    for line in file:
        print(line.strip())