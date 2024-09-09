import pandas
data = pandas.read_csv("NATO.csv")
# print(data)
new_dict = {row.letter:row.code for (index,row) in data.iterrows()}
# print(new_dict)
user_input = input("Enter the word for NATO Conversion  ").upper()
NATO_list= [new_dict[letter] for letter in user_input ]
print(NATO_list)