# FIZZ-BUZZ Problem
maxNumber = int(input("Enter a Max Number upto which u want to Print Fizz-Buzz Solution : "))
for number in range(1,maxNumber+1):
  if(number%3==0 and number%5==0):
    print("FizzBuzz")
  elif(number%3==0):
    print("Fizz")
  elif(number%5==0):
    print("Buzz")
  else:
    print(number)