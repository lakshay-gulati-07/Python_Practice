
def add(n1,n2):
  return n1+n2

def sub(n1,n2):
  return n1-n2

def mul(n1,n2):
  return n1*n2

def div(n1,n2):
  return n1/n2

operation = {
  "+" : add,
  "-" : sub,
  "*" : mul,
  "/" : div
}
want_to_continue = True
num1 = int(input("Enter first number "))
for operators in operation:
  print(operators)
choice = input("Choose one operations from above ")
num2 = int(input("Enter Second number "))
funtion = operation[choice]
result = funtion(num1,num2)
print(f"{num1} {choice} {num2} = {result}")
while want_to_continue:
  wish = input("Do you want to continue ?? y for yes/n for no \n")
  if wish == "y":
    num3 = input("Enter a Number ")
    num2 = result
    for operators in operation:
      print(operators)
    choice = input("Choose one operations from above ")
    funtion = operation[choice]
    result = funtion(num1,num2)
    print(f"{num3} {choice} {num2} = {result}")
  else:
    want_to_continue = False





