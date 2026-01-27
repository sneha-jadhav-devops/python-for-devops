try:
    number = int(input("Enter a number: "))
    print("Number entered:", number)
except ValueError:
    print("Invalid input. Please enter a number.")
finally:
    print("Execution completed")
