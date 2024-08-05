n = int(input("Enter a number "))
def prime_checker(number):
  sum = 0
  for i in range(1,number):
    if number % i == 0:
      sum +=1

  if sum>1:
    print(f"{number} is not a prime number ")
  else:
    print(f"{number} is a prime number")
      
prime_checker(number = n)