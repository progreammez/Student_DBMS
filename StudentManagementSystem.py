import time
#Take input from user and store in a list. THe list is the database and use it to access or delete
print("Welcome to Student Database System!")
time.sleep(1)
details = {
    101: { "name" : "Mrudu", "course" : "Python" },
    102: { "name" : "Rohan", "course" : "C++" },
    103: { "name" : "Akshay", "course" : "Java" },
    104: { "name" : "Tanvi", "course" : "JavaScript" },
    105: { "name" : "Chitraksh", "course" : "C" }
}
while True:
    print("""\n
Press '1' to view a student's details
Press '2' to add a new student
Press '3' to update a student's details
Press '4' to delete a student's details
Press '5' to exit""")
    initial_input = int(input())

    #ViewDetails
    if initial_input == 1:
        while True:
            print("""What do you wanna view?
1. A particular student's details
2. Full database""")
            view_input = int(input())
            if view_input == 1:
                view_roll = int(input("Enter the student's roll number: "))
                if view_roll in details:
                    print(f"Name: {details[view_roll]['name']}")
                    print(f"Course: {details[view_roll]['course']}")
                else:
                    print("Roll number not found.")
                break
            elif view_input == 2:
                if len(details) == 0:
                    print("Database is empty.")
                else:
                    for roll, info in details.items():
                        print(f"Roll number: {roll}")
                        print(f"Name: {info['name']}")
                        print(f"Course: {info['course']}")
                break
            else:
                print("Enter a valid response.")
            
    #AddDetails
    elif initial_input == 2:
        last_roll = max(details.keys())
        new_roll = last_roll + 1
        name_add = input("Enter the name of the student: ")
        course_add = input("Enter the course enrolled in: ")
        details[new_roll] = {"name": name_add, "course": course_add}
        time.sleep(1)
        print(f"The student's details have been succesfully added with roll number {new_roll}.")

    #UpdateDetails
    elif initial_input == 3:
        update_roll = int(input("Enter the roll number of the student: "))
        if update_roll in details:
            while True:
                print("""What details do you want to update?
1. Update Name
2. Update Courses""")
                details_update = int(input())
                if details_update == 1:
                    name_update = input("Enter the updated name: ")
                    details[update_roll]["name"] = name_update
                    print(f"The details of the {update_roll} roll number has been successfully updated.")
                    break
                elif details_update == 2:
                    course_update = input("Enter the updated course: ")
                    details[update_roll]["course"] = course_update
                    print(f"The details of the {update_roll} roll number has been successfully updated.")
                    break
                else:
                    print("Enter a valid response.")  
        else:
            print("Roll number not found.")  

    #DeleteDetails
    elif initial_input == 4:
        while True:
            delete_roll = int(input("Enter the roll number of the student: "))
            if delete_roll in details:
                confirm_delete = input("Are you sure you want to delete the student?(y/n)")
                if confirm_delete.lower() == 'y':
                    del details[delete_roll]
                    print(f"Student with roll number {delete_roll} has been deleted.")
                    break
                else:
                    print("Deletion cancelled. No changes made.")
            else:
                print("Roll number not found.")
    
    #Exiting
    elif initial_input == 5:
        print("Thank you for using Student Database System.")
        break

    #Error
    else:
        print("Enter a valid response.")
