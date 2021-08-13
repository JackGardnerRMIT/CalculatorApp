while True:

    num1 = input("First number:")
    num2 = input("Second number:")

    type = input(str("Please input the type: (+, -, *, /) Press space and enter to stop the program."))

    num1 = int(num1)
    num2 = int(num2)

    if type == "+":
        result1 = num1 + num2
        print(result1)
    elif type == "-":
        result2 = num1 - num2
        print(result2)
    elif type == "*":
        result3 = num1 * num2
        print(result3)
    elif type == "/":
        result4 = num1 / num2
        print(result4)
    elif type == " ":
        print("Thanks for using me!")
        break
    else:
        print("Opps wrong data type, please try again.")