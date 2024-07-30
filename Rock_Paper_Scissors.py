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


group = [rock,paper,scissors]
choice = int(input("Enter your choice 0 for rock, 1 for paper , 2 for scissors\n"))
print(f"you choose {group[choice]}")
computer_choice= random.randint(0,2)
print(computer_choice)
print(f"Computer chooses {group[computer_choice]}")
if(choice==computer_choice):
  print("ITS a Draw !!")
elif(choice==0 and computer_choice==2):
  print("YOU WON !!")
elif(choice==1 and computer_choice==0):
  print("YOU WON")
elif(choice==2 and computer_choice==1):
  print("YOU Won")
else:
  print("computer Won NT !!")
