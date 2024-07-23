alphabet = ["",'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',"",'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def encrypt(plain_text, shift_amount):
  new_text = ""
  for letter in plain_text:
    index_of_letter = alphabet.index(letter)
    new_text += alphabet[index_of_letter+shift_amount]
  print(new_text)



def decrypt(encrypted_text,shift_amount):
  normal_text = ""
  for letter in encrypted_text:
    index_of_encrptedLetter = alphabet.index(letter)
    normal_text += alphabet[index_of_encrptedLetter-shift_amount]
  print(normal_text)




want_to_continue = True
while want_to_continue:
  direction = input("Choose option from below \n 1. write encode to encrypt message \n 2. write decode to decrypt \n")
  text = input("Type your message without spaces:\n").lower()
  shift = int(input("Type the shift number:\n"))
  if direction == "encode":
    encrypt(plain_text=text , shift_amount=shift)
  elif direction == "decode":
    decrypt(encrypted_text=text , shift_amount=shift)
  else:
    print("Wrong choice !!")
    want_to_continue = False
  choice = input("Do you want to continue y/n  ")
  if choice == "y":
    want_to_continue = True
  else:
    want_to_continue = False
  