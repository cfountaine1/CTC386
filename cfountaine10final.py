#cfountaine10
#Final project
#Menu
#include a loop
#include a conditional statement
#include user input
#include a function

def celsius(c):
    celsius =(Fahrenheit - 32) * 5/9
    return celsiusconversion
def Fahrenheit(f):
    f= int(input("Enter the current temperature in Fahrenheit.  "))
    print("The temperature in celsius is   ", celsius)
def challenge():
    print("Guess my favorite cartoon character!")
secret_word = "morty"
guess = "   "
guess_count = 0

name = input("What is your name?   ")
print("Hello",name,"Look at the menu")
print("     Menu     ")
print("______________:")

print("Option 1: Tell me a joke")
print("Option 2: Say my name like Destiny's Child 15x ")
print("Option 3: Hear a famous quote ")
print("Option 4: Guess a number.")
print("Option 5: Celsius conversion")
print("Option 6: Guess my secret cartoon character")
print("__________________")

print("Hello", name,".")
option = int(input ("Enter option number   "))
print("Enter an option number:   ")
if (option ==1):
    print (name, "What do you call little snowmen? ......... Chilllllldren!:")
elif (option ==2):
    for i in range(15):
        print (name)
elif (option == 3):
    num = int(input( "Ok, tell me the number of times you want to see your quote: "))
    for i in range(num):
        print ("Nobody puts baby in the corner.")
elif (option == 4):
    secretNumber =67
    guess = 0
    while (guess !=secretNumber):
        guess = int(input("Guess the secret number between 1-100:    "))
        if (guess<secretNumber):
            print ("Good try, but it needs to be higher, guess agaian.")
        elif (guess>secretNumber):
            print ("Good try, but it needs to be lower, guess again.")
        elif (guess==secretNumber):
            print ("Yay! You nailed it!")

elif (option==5):
    Fahrenheit=int(input("Enter the current temperature in Fahrenheit."))
    celsius=Fahrenheit - 32 * 5/9
    print ("The current temperature in celsius is:  ", celsius)

elif (option==6):
    print("Guess my favorite cartoon character.")
    guess = input ("Enter a word:   ")
while guess != secret_word:
    guess = input("Wrong guess! Try another character name:  ")
    if guess == secret_word:
        print ("You have won!")

