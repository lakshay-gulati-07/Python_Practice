import random
random_number = random.randrange(1,100)
print(random_number)
logo = """
  ____                       _____ _                                
 / ___|_   _  ___  ___ ___  |_   _| |__   ___                       
| |  _| | | |/ _ \/ __/ __|   | | | '_ \ / _ \                      
| |_| | |_| |  __/\__ \__ \   | | | | | |  __/                      
 \____|\__,_|\___||___/___/   |_| |_| |_|\___|   

                                          ____
| \ | |_   _ _ __ ___ | |__   ___ _ __   / ___| __ _ _ __ ___   ___ 
|  \| | | | | '_ ` _ \| '_ \ / _ \ '__| | |  _ / _` | '_ ` _ \ / _ /
| |\  | |_| | | | | | | |_) |  __/ |    | |_| | (_| | | | | | |  __/
|_| \_|\__,_|_| |_| |_|_.__/ \___|_|     \____|\__,_|_| |_| |_|\___|


"""

print(logo)

game_mode =input("Welcome to Number Guessing Game\nChoose between 'hard' and 'easy' mode ")
if game_mode == "hard":
  life = 5
  print(f"Life for Hard mode is {life}")
elif game_mode =="easy":
  life = 10
  print(f"life for Easy Mode is {life}")
else:
  print("Wrong option is choosen")
  life = 0
  
while life > 0:
  user_guess = int(input("Guess a Number 1-100 "))
  
  if life == 0:
    print("You Loose, No life Remaining")
  
  elif user_guess == random_number:
    print("Congratulations !! You've Guessed the Number")
    life = 0
  
  elif user_guess > random_number:
    life -= 1
    print(f"Too High, Guess Again, lifes Remaining {life}")
    
  elif user_guess < random_number:
    life -= 1
    print(f"Too Low, Guess Again, lifes remaining {life}")

  
  
  

