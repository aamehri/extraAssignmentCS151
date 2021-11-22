# Extra Assignment for CS151
def add_student(stu_data):
    print("Student Utility")
    student_ID = input("Enter a unique student ID: ")
    student_name = input("Enter the student name: ")
    stu_data[student_ID] = [student_name, 0.0, 0.0, 0.0]


def menu():
    print("Utility Menu\n"
          "============\n"
          "0. Load students from file\n"
          "1. Add Students\n"
          "2. Add grades\n"
          "Report Menu\n"
          "===========\n"
          "3. Run Report\n"
          "4. EXIT")
    choice = input("Enter your choice: ")
    return choice

def main():
    students = {} # key student ID, names and grades will be payload
    option = '0'
    while option != '4':
        option = menu()
        if option == '1':
            add_student(students)

    print(students)
main()