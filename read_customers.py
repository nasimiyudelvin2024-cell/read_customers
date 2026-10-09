# Task 24: Reading Customer Records
import os

# Create a sample file only if it does not exist (for testing)
if not os.path.exists("customers.txt"):
    with open("customers.txt", "w") as s:
        s.write("Grace Achieng, 0712345678\nSam Mwangi, 0723456789\n")

f = open("customers.txt", "r")
contents = f.read()
print(contents)
f.close()

print("File modes:")
print("r - read: opens an existing file for reading only (error if missing).")
print("w - write: creates a file or overwrites existing contents.")
print("a - append: adds new data at the end without erasing existing data.")
