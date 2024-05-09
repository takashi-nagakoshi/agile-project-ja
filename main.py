import math



print("Select operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")
print("5. Exponent")
print("6. Square Root")

while True:
    choice = input("Enter choice (1/2/3/4/5/6): ")

    if choice in ('1', '2', '3', '4', '5', '6'):
        num1 = float(input("Enter first number: "))

        if choice != '6':
            num2 = float(input("Enter second number: "))

        if choice == '1':
            print("Result:", add(num1, num2))
        elif choice == '2':
            print("Result:", subtract(num1, num2))
        elif choice == '3':
            print("Result:", multiply(num1, num2))
        elif choice == '4':
            print("Result:", divide(num1, num2))
        elif choice == '5':
            print("Result:", exponent(num1, num2))
        elif choice == '6':
            print("Result:", square_root(num1))
    else:
        print("Invalid input")