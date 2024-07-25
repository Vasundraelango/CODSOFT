
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

while True:
    num1 = int(input("Please enter the first number: "))
    num2 = int(input("Please enter the second number: "))

    print("Please select the operation.")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")

    choice = input("Please enter choice : ")

    if choice == '5':
        print("Exiting calculator. Goodbye!")
        break

    elif choice == '1':
        print("Result is: ", num1 ," + ", num2 , " = " , add(num1, num2))
 
    elif choice == '2':
        print("Result is: ", num1 ," - ", num2 , " = " , subtract(num1, num2))

    elif choice == '3':
        print("Result is: ", num1 ," * ", num2 , " = " , multiply(num1, num2))

    elif choice == '4':
        
        print("Result is: ", num1 ," / ", num2 , " = " , divide(num1, num2))


    else:
        print("Invalid input...")

    
    next_action = input("Do you want to perform another calculation? (yes/no): ").lower()
    if next_action != 'yes' and next_action != 'y':
        print("Thank you!")
        break
