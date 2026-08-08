student = {}

while True:
    print("\n-------STUDENT MANAGER APP-------")
    print("1. Add Student")
    print("2. View Student")
    print("3. Check result")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if(choice == "1"):
        name = input("Enter student name: ")
        marks = int(input("Enter students marks: "))
        student [name] = marks
        print(f"{name} Successfully Updated!")

    elif choice == "2": 
        if not student:
            print("No student found!")
        else:
            for name, marks in student.items():
                print(name, ":", marks)   

    elif choice == "3":
        name = input("Enter Student name: ")

        if name in student:
            marks = student[name]

            if marks >=40 :
                print("pass")
            else:
                print("fail")
        else:
            print("Student not found :( ")

    elif choice == "4":
        break
    else:
        print("Invalid no.")
print("Thank you")         

