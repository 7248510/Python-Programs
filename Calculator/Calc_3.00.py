def choice():
    statement()
    option = eval(input()) #Setting the options to their given functions 
    if option == 1:
        addition() #Addition Module
    if option == 2:
        subtracting() #Subtraction Module
    elif option == 3:
        division() #Floating Division Module
    elif option == 4:
        division_Float() #Division module
    elif option == 5:
        multiplication()
    #Space between the IF statements & the function code.
    takeback()
def statement():
    print("Enter one for addition.\nEnter two for subtraction.\nEnter three for division.\nEnter four for floating division.\nEnter five for multiplication.") 
def addition():
    print("You picked addition.") #Outputting what the user picked.
    a = float(input("Please your first number "))
    b = float(input("Please enter your second number "))
    answer = a + b
    print("The operation you did was", a, "+",b,".")
    print("Your answer is:", answer,)
    #Gives the user an option to restart the program.
    #Space between the module/function.
    return
def subtracting():
    print("You picked subtraction!")
    a = float(input("Enter your first number "))
    b = float(input("Enter a second number "))
    answer = a - b
    print("The operation you did was", a, "-",b,".")
    print("Your answer is:", answer,)
    #Gives the user an option to restart the program.
    #Space between the module/function.
def division_Float():
    print("You picked division with floats!")
    a = int(input("Enter your first number "))
    b = int(input("Enter a second number "))
    answer = a // b
    print("The operation you did was", a, "/",b,".")
    print("Your answer is:", answer,)
    print("Their is nothing wrong with the math, we are dividing integers & leaving the decimals out by using floating division.\nCheck the source code, the slashes are different.")
    #Gives the user an option to restart the program.
    #Space between the module/function.
def division():
    print("You picked division!")
    a = float(input("Enter your first number "))
    b = float(input("Enter a second number "))
    answer = a // b
    print("The operation you did was", a, "//",b,".")
    print("Your answer is:", answer,)
    #Gives the user an option to restart the program.
    #Space between the module/function.
def multiplication():
    print("You picked multiplication!")
    a = float(input("Enter your first number "))
    b = float(input("Enter a second number "))
    answer = a * b #Multiplication
    print("The operation you did was", a, "*",b,".")
    print("Your answer is:", answer,)                     #Gives the user an option to restart the program.
    #Space between the module/function.
def takeback(): #The purpose of this function is to restart the program.
    question = eval(input("Would you like to restart the program?\nPlease enter True or False.\n"))
    if question == True: #1 is a trigger for yes/true
        print("Restarting")
        choice() #Restarts the program/re-runs the function.
    elif question == False: #2 is a trigger for no/false
        pass #Goes directly back to the function & does nothing.
    return        
choice()
