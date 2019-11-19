#!/usr/bin/python
def statement():
    print("Enter one for addition.\nEnter two for subtraction.\nEnter three for division.\nEnter four for floating division.\nEnter five for multiplication!") #Explaining the programs functions.
    option = input() #Setting the options to their given functions 
    if option == 1:
        addition() #Addition Module
    elif option == 2:
        subtracting() #Subtraction Module
    elif option == 3:
        division() #Floating Division Module
    elif option == 4:
        division_Float() #Division module
    elif option == 5:
        multiplication()
    #Space between the IF statements & the function code.
def addition():
    print("You picked addition.") #Outputting what the user picked.
    a = float(input("Please your first number "))
    b = float(input("Please enter your second number "))
    answer = a + b
    print"The operation you did was", a, "+",b,"."
    print"Your answer is:", answer,
    takeback() #Gives the user an option to restart the program.
#Space between the module/function.
def subtracting():
    print("You picked subtraction!")
    a = float(input("Enter your first number "))
    b = float(input("Enter a second number "))
    answer = a - b
    print"The operation you did was", a, "-",b,"."
    print"Your answer is:", answer,
    takeback() #Gives the user an option to restart the program.
#Space between the module/function.
def division_Float():
    print("You picked division with floats!")
    a = int(input("Enter your first number "))
    b = int(input("Enter a second number "))
    answer = a // b
    print"The operation you did was", a, "/",b,"."
    print"Your answer is:", answer,
    print("Their is nothing wrong, we are dividing integers & leaving the decimals out by using floating division.\nCheck the source code, the slashes are different.")
    takeback()                      #Gives the user an option to restart the program.
#Space between the module/function.
def division():
    print("You picked division!")
    a = float(input("Enter your first number "))
    b = float(input("Enter a second number "))
    answer = a // b
    print"The operation you did was", a, "//",b,"."
    print"Your answer is:", answer,
    takeback()                      #Gives the user an option to restart the program.
#Space between the module/function.
def multiplication():
    print("You picked multiplication!")
    a = float(input("Enter your first number "))
    b = float(input("Enter a second number "))
    answer = a * b #Multiplication
    print"The operation you did was", a, "*",b,"."
    print"Your answer is:", answer,
    takeback()                      #Gives the user an option to restart the program.
#Space between the module/function.
def takeback(): #The purpose of this function is to restart the program.
    takeback = input("\nDo you want to restart the program?\nOne for yes & two for no. ")
    if takeback == 1: #1 is a trigger for yes/true
        print("Restarting")
        statement() #Restarts the program/re-runs the function.
    elif takeback == 2: #2 is a trigger for no/false
        pass #Goes directly back to the function & does nothing.
statement() #The big function
