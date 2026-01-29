#cfountainefinal1.py
#Ask a user to choose between 3 different options.
#Option 1 will ask the user for their name and print out a joke using that name.
#Option 2 will display the name of a food 20 times.
#Option 3 will continue to ask the user to input a number until they enter 0. If the user enters any other number display a warning.

userInput=None
("Hello,Look at the choices below.")
print ("       3 Options       ")
print ("___________________________")

print("Option 1: Tell me a joke")
print("Option 2: What's for dinner?")
print("Option 3: The number game.")
option = int(input("Enter an option number   "))
print("Enter an option number   ")
if(option==1):
    name = input("Tell me your name.    ")
    print(name, "What do you call a sleeping bull? A bulldozer! Do you get it?",name,)
if(option==2):
    for i in range(20):
        print("lasagna")
if (option==3):
    while userInput !=0:
        userInput= int(input("Enter a number:   "))
        print("Enter 0 or else imminent doom awaits.")
    if (userInput>0):
        if(userInput<0):
            print("Enter 0 or else imminent doom awaits.")
    if (userInput==0):
        print("There it is, I knew you could do it.")
