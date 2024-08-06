import random
testseed = int(input("Enter a seed number "))
random.seed(testseed)
name = input("Enter name separated by comma ")
name_list = name.split(",")
length = len(name_list)
random_number = random.randint(0,length) - 1
random_name = name_list[random_number]
print(f"{random_name} is going to pay bill")