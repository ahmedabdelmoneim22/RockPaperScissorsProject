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
import random
rock_paper_scissors=[rock,paper,scissors]
Your_choose=int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
print(rock_paper_scissors[Your_choose])
computer_choice=random.randint(0,2)
print("Computer chose:")
print(rock_paper_scissors[computer_choice])
if Your_choose >= 3 or Your_choose < 0:
  print("You typed an invalid number, you lose!")
elif Your_choose == 0 and computer_choice == 2:
  print("You win!")
elif computer_choice == 0 and Your_choose == 2:
  print("You lose")
elif computer_choice > Your_choose:
  print("You lose")
elif Your_choose > computer_choice:
  print("You win!")
elif computer_choice == Your_choose:
  print("It's a draw")