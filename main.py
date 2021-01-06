
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

your_choice =int(input("Please choose..\n"+ rock +"\n" + paper +"\n" + scissors +"by choosing 0, 1, 2\n" ))

choices = [rock, paper, scissors]
computer_choice = random.randint(0,2)

if your_choice >= 0 and your_choice <= 2:

  print(f"Computer choose:\n{choices[computer_choice]}\n {computer_choice}")
 
  print(f"You choose:\n{choices[your_choice]}\n{your_choice}" )

  if computer_choice == your_choice:
    print("draw")
  elif your_choice == 0  and computer_choice == 2:
    print("you win")
  elif computer_choice == 0 and your_choice == 2:  
    print("you loose")
  elif computer_choice > your_choice:
    print("you loose")
  else:
    print("you win")
else:
  print("You choose an invalid number, you loose.")  
    

