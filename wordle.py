import random

list_of_words = [
    "harmony", "explore", "inspire", "create", "imagine", "discover", "believe",
    "achieve", "wisdom", "courage", "passion", "purpose", "freedom", "kindness",
    "justice", "peace", "unity", "strength", "growth", "vision", "integrity",
    "respect", "trust", "gratitude", "compassion", "innovation", "adventure",
    "knowledge", "empower", "transform", "resilience", "optimism", "determination",
    "faith", "hope", "joy", "love", "balance", "nature", "serenity", "challenge",
    "focus", "curiosity", "creativity", "patience", "humility", "generosity",
    "dedication", "leadership", "perseverance", "truth", "bravery", "humor",
    "enthusiasm", "reflection", "wisdom", "loyalty", "ambition", "clarity",
    "determination", "efficiency", "empathy", "encouragement", "forgiveness",
    "friendship", "grace", "growth", "honesty", "improvement", "independence",
    "justice", "learning", "liberty", "love", "motivation", "patience", "peace",
    "positivity", "productivity", "progress", "reliability", "respect", "responsibility",
    "satisfaction", "self-discipline", "service", "sincerity", "solidarity", "spirit",
    "stability", "success", "support", "trust", "understanding", "wellness", "wisdom"
]
random_word = random.choice(list_of_words)
length = len(random_word)
dash_list = []

for letter in random_word:
    dash_list.append("_")

print(dash_list)
print(f"The word consists of {length} letters ")

life = 7 

in_game = True
while in_game:
    count = 0
    guess = input(f"Guess a letter, life reamaining {life} ").lower()
    for i in random_word:
        if guess == i:
            dash_list[count] = guess
            print("You've guessed correct letter")
        count +=1
    print(dash_list)
    if guess not in random_word:
            life -=1
            print(f"{guess} is not in Word, Enter a different letter and life reamaining {life}")
    if life ==0:
      print(f"You Don't have life reamaining :(  Game Over !! \n The Word was {random_word}")
      in_game = False
    if "_" not in dash_list:
      print(f"you have guessed the word '{random_word}', You Won GG !!")
      in_game = False
            