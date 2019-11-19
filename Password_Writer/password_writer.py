def statement():
    print("1 = Write, 2 = Restart, 3 = Delete")
def username():
    f= open(input("Please enter the name with .txt "), "w+") #The w+ = the file action mode(R = read w = write)
    f.write("Username:" + input("Enter your Username ")  +"\n" )
    f.write("Password:" + input("Enter your password ") + "\n")
    f.write("Website:" + input("Enter the website you want ") + "\n")
#Space
def read():
    f=open("Password.txt", "r+") #Reads the file that we just created
    read_me = f.read() #Setting a variable to the read function
    print(read_me) #Prints the file we created
#Space
def restart():
    print("The program has restarted please enter, 1 = Write, 2 = Restart, 3 = Delete")
    statement()
    choice()
def delete():
    import os
    cwd = os.getcwd()
    os.listdir(cwd)
    print(os.listdir(cwd))
    print("Please select the file that you selected.")
    delete_me=input()
    if os.path.isfile(delete_me):
        print("Your file has %s been deleted."% (delete_me))
        os.remove(delete_me)
    else:
        print("Your file is not here.")
#space    
def choice():
    selection = eval(input())
    if (selection == 1):
        print("We are going to write a password file.")
        username()
    if (selection == 2):
        print("We are going to restart the program.")
        restart()
    if (selection == 3):
        print("We are going to delete the file you created.")
        delete()
statement()
choice()

