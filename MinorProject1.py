print("Select an operation:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

while True:
    choice = input("Make a choice (1/2/3/4): ")

    if choice in ['1', '2', '3', '4']:
        num1 = float(input("Enter 1st number: "))
        num2 = float(input("Enter 2nd number: "))

        if choice == '1':
            result = num1 + num2
            operation = "addition"
        elif choice == '2':
            result = num1 - num2
            operation = "subtraction"
        elif choice == '3':
            result = num1 * num2
            operation = "multiplication"
        elif choice == '4':
            if num2 == 0:
                print("Error! Division by zero.")
                continue
            result = num1 / num2
            operation = "division"

        print(f"The result of {operation} is: {result}")
    else:
        print("Invalid input! Please select from (1/2/3/4)!")

    next_calculation = input("Do you want to perform another calculation? (yes/no): ")
    if next_calculation.lower() != 'yes':
        break
