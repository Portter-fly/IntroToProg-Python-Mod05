# ------------------------------------------------------------------------------------------ #
# Title: Assignment05
# Desc: This assignment demonstrates using lists and files to work with data
# Change Log: (Who, When, What)
#   RRoot,1/1/2030,Created Script
#   Hao Yi Fei,11/9/2025, iteration
# ------------------------------------------------------------------------------------------ #

import json
import io as _io

# Define Data Constants
MENU: str = '''
    ---- Course Registration Program ----
      Select from the following menu:  
        1. Register a Student for a Course.
        2. Show current data.  
        3. Save data to a file.
        4. Exit the program.
    ----------------------------------------- 
    '''
FILE_NAME: str = "Enrollments.json"
NON_SPEC_ERROR_MESSAGE:str = "There was a non-specific error!\n"
TECH_ERROR_MESSAGE:str = "-- Technical Error Message --\n"

# Define Data Variables
student_first_name: str = ''  # Holds first name of a student entered by user.
student_last_name: str = ''  # Holds last name of a student entered by user.
course_name: str = ''  # Holds the name of a course entered by the user.
student_data: dict = {}  # One row of student data (Now a Dictionary)
students: list = []  # A table of student data
file = _io.TextIOWrapper  # Holds a reference to an opened file.
menu_choice: str = ''  # Hold the choice made by the user.


try:
    file = open(FILE_NAME, "r")
    students = json.load(file)
    file.close()
# Exception Handling
except FileNotFoundError as e:
    print("Text file must exist before running this script!\n")
    print(TECH_ERROR_MESSAGE)
    print(e, e.__doc__, type(e), sep='\n')
except Exception as e:
    print(NON_SPEC_ERROR_MESSAGE)
    print(TECH_ERROR_MESSAGE)
    print(e, e.__doc__, type(e), sep='\n')
finally:
    if not file.closed: file.close()

# Present and Process the data (Main Menu Loop)
while True:

    # Present the menu of choices
    print(MENU)
    menu_choice = input("What would you like to do: ")

    # Input user data (Add Data)
    if menu_choice == "1":

        while student_first_name == "" or student_last_name == "":
            try:
                # First Name
                while student_first_name == "":
                    student_first_name = input("Enter the student's first name: ")
                    if not student_first_name.isalpha():
                        student_first_name = ""
                        raise ValueError("The first name should not contain numbers.")

                # Last Name
                while student_last_name == "":
                    student_last_name = input("Enter the student's last name: ")
                    if not student_last_name.isalpha():
                        student_last_name = ""
                        raise ValueError("The last name should not contain numbers.")
                course_name = input("Please enter the name of the course: ")
                student_data = {"FirstName": student_first_name,
                                "LastName": student_last_name,
                                "CourseName": course_name}
                students.append(student_data)
                print(f"You have registered {student_data['FirstName']}",
                      f"{student_data['LastName']} for",
                      f"{student_data['CourseName']}.")

            # Exception Handling
            except ValueError as e:
                print(e)
                print(TECH_ERROR_MESSAGE)
                print(e.__doc__)
                print(e.__str__())
            except Exception as e:
                print(NON_SPEC_ERROR_MESSAGE)
                print(TECH_ERROR_MESSAGE)
                print(e, e.__doc__, type(e), sep='\n')

        # After valid name input, reset name to allow multiple registrations
        student_first_name = ""
        student_last_name = ""

        continue  # Go back to Main Menu Loop

    # Present the current data (Show Data)
    elif menu_choice == "2":
        print("-"*50)
        for student in students:
            print(student["FirstName"], student["LastName"],
                  student["CourseName"], sep = ",")
        print("-"*50)

        continue

    # Save the data to a file (Save Data)
    elif menu_choice == "3":
        try:
            file = open(FILE_NAME, "w")
            json.dump(students, file, indent = 4)
            file.close()

            # Display what was written to the file using the students variable
            print("The following data was saved to file!")
            for student in students:
                print(f"Student {student['FirstName']} {student['LastName']}",
                      f"is enrolled in {student['CourseName']}")

        # Exception Handling
        except TypeError as e:
            print("Please check that the data is a valid JSON format\n")
            print(TECH_ERROR_MESSAGE)
            print(e, e.__doc__, type(e), sep='\n')
        except Exception as e:
            print(NON_SPEC_ERROR_MESSAGE)
            print(TECH_ERROR_MESSAGE)
            print(e, e.__doc__, type(e), sep='\n')
        finally:
            if not file.closed: file.close()

        continue

    # Exit Program
    elif menu_choice == "4":
        break
    else:
        print("Please only choose option 1, 2, 3, or 4")
print("Program Ended")