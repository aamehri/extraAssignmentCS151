# Extra Assignment for CS151

def menu():
    print("Utility Menu\n"
          "============\n"
          "1. Add Students\n"
          "2. Add grades\n"
          "Report Menu\n"
          "===========\n"
          "3. Run Report\n"
          "4. EXIT")
    choice = input("Enter your choice: ")
    return choice

def main():
    option = '0'
    while option != '4':
        option = menu()
main()