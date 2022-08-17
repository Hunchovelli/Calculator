import math

answer = input("Do you want to perform an operation ")



while (answer.lower() == "yes" or answer.lower() == "y"):

    print ("""Select an operation:

    1. Add
    2. Subtract
    3. Multiply
    4. Divide
    5. Square Root
    6. Power
    
    """)

    operation = input("Which operation would you like to do: ")

    if (operation.lower() == "add" or operation.lower()  == "1"):
        num1 = input("Enter number: ")
        num2 = input("%s + " %str(num1))
        result = int(num1) + int(num2)
        print (result)  
        answer = input("Do you want to perform another operation? ")  
    elif (operation.lower()  == "subtract" or operation.lower()  == "2"):
        num1 = input("Enter number: ")
        num2 = input("%s - " %str(num1))
        result = int(num1) - int(num2)
        print (result)
        answer = input("Do you want to perform another operation? ")
    elif (operation.lower()  == "multiply" or operation.lower()  =="3"):
        num1 = input("Enter number: ")
        num2 = input("%s * " %str(num1))
        result = int(num1) * int(num2)
        print (result)
        answer = input("Do you want to perform another operation? ")
    elif (operation.lower()  == "divide" or operation.lower()  == "4"):
        num1 = input("Enter number: ")
        num2 = input("%s / " %str(num1))
        result = int(num1) / int(num2)
        print (result)
        answer = input("Do you want to perform another operation? ")
    elif (operation.lower()  == "square root" or operation.lower() == "5"):
        num1 = input("Enter number: ")
        result = math.sqrt(int(num1))
        print (result)
        answer = input("Do you want to perform another operation? ")
    elif (operation.lower()  == "power" or operation.lower() == "6"):
        num1 = input("Enter number: ")
        num2 = input("%s raised to the power of " %str(num1))
        counter = 1
        result = int(num1)
        while counter < int(num2):
            result *= int(num1) 
            counter += 1
        print (result)
        answer = input("Do you want to perform another operation? ")
    else:
        print ("""Select an operation:
    1. Add
    2. Subtract
    3. Multiply
    4. Divide
    5. Square Root
    6. Power""")
        operation = input("/nInvalid Input please enter again ")



    







