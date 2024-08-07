import random
import dataValue
def comparison():
  comp1 = random.choice(dataValue.data)
  return comp1

in_game = True
while in_game:
  print(dataValue.logo_Higher_Lower)
  print("Compare Between 'A' and 'B' \nWho is having More Followers")
  game_continue = True
  count = 0
  while game_continue:
    comp1 = comparison()
    print(f"A ----> {comp1['''name'''], comp1['description'], comp1['country']}")
    print(comp1["follower_count"])
    print(dataValue.logo_VS)
    comp2 = comparison()
    if comp1 == comp2 :
      comp2 = comparison()
    print(f"\nB ----> {comp2['name'], comp2['description'], comp2['country']}")
    print(comp2["follower_count"])
    choice = input("Choose Between 'A'or 'B' ---> ").upper()
    if choice == "A" and comp1["follower_count"] > comp2["follower_count"]:
      count += 1
      comp2 = comparison()
      print(f"Current Score = {count}")
    elif choice == "B" and comp1["follower_count"] < comp2["follower_count"]:
      count += 1
      comp1 = comp2
      comp2 = comparison()
      print(f"Current Score = {count}")
    else:
      game_continue = False
      print(f"You Loose !! with a Score of {count}")
  choice = input("Do You want to continue ? Y/N ").upper()
  if choice == "Y":
    in_game = True
    
  else:
    in_game = False



  

