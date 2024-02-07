number1 = ""
number2 = ""
while number1 != 0 and number2 != 0:
    number1 = int(input("Enter a Number: "))
    number2 = int(input("Enter a second Number: "))
    if number1 == number2:
        print("The Numbers are Equal")
    elif number1 > number2:
        print(number1)
    else:
        print(number2)

print("end of program")