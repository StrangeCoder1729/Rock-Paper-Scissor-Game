
import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

choices = [rock,paper,scissors]

print("WELCOME TO ROCK,PAPER,SCISSORS GAME !!")
print("Type 1 for Rock")
print("Type 2 for Paper")
print("Type 3 for Scissors")
print()

########################################################## For user ############################################################################# 
user_choice = int(input("Enter Your Choice : "))
if user_choice == 1:print(choices[0]) 
elif user_choice == 2 :print(choices[1])
elif user_choice == 3 :print(choices[2])
else: 
    print("You chose a wrong input , so henceforth you have lost the game")
    exit()



########################################################## For Computer ############################################################################# 
computer_choice = random.randint(1,len(choices))
# print(computer_choice)
if computer_choice == 1:print(choices[0])
elif computer_choice == 2 :print(choices[1])
elif computer_choice == 3 :print(choices[2])

########################################################## Logic ############################################################################# 

if user_choice == 1:  #Rock
    if computer_choice == 1:
        print("IT IS A TIE !!")
    elif computer_choice == 2:
        print("COMPUTER WINS AND YOU LOOSE !!")
    elif computer_choice == 3:
        print("YOU WON !!")

elif user_choice == 2:  #Paper
    if computer_choice == 1:
        print("YOU WON !!")
    elif computer_choice == 2:
        print("IT IS A TIE !!")
    elif computer_choice == 3:
        print("COMPUTER WINS AND YOU LOOSE !!")

elif user_choice == 3:   #Scissors
    if computer_choice == 1:
        print("COMPUTER WINS AND YOU LOOSE !!!")
    elif computer_choice == 2:
        print("YOU WIN AND COMPUTER LOOSES !!")
    elif computer_choice == 3:
        print("IT IS A TIE !!")


    



