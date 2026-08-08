import random
import string

passwords = {}

try:
    with open("Password.txt", "r") as file:
        for line in file:
            website, pwd = line.strip().split(":")
            passwords[website] = pwd
except:
    pass

def generate_pass():
    chars = string.ascii_letters + string.digits + "!@#$%^&*"
    password = "".join(random.choice(chars) for _ in range(8))
    return password

while True:
     print("\n------- Password Manager-------")
     print("1. Save Pass")
     print("2. View Passwords")
     print("3. Generate pass")
     print("4. Exit")

     choice = input("Enter your choice: ")

     if choice == "1":
         site = input("Enter website: ")
         pwd = input("Enter pass: ")

         passwords[site] = pwd

         with open ("Password.txt", "w") as file:
             file.write(f"{site}:{pwd}\n")

         print("Saved")

     elif choice == "2":
         if not passwords:
             print("No data")
         else:
             for site, pwd in passwords.items():
                 print(site, ":", pwd)
     elif choice == "3":
        print("Generated pass", generate_pass())

     elif choice == "4":
         print("Ok Good bye!!")
         break
     else:
         print("Invalid no.") 

