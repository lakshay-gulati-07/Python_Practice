list1 = [1,2,3,4,5]
name = "Lakshay"

#normal list Comprehension 👇
#       new_list = [new_item for item in list]

new_list1 = [item * 2 for item in list1]
new_list2 = [letter for letter in name]
new_list3 = [item *2 for item in range(1,5)]




#  conditional List Ccomprehension 👇
#       new_list = [new_item for item in list if test]

new_list4 = [number for number in range(1,31) if number%2 ==0]
names_list = ["Vikas","Roshan","Ishan","Lakshay"]
new_list5 = [name for name in names_list if len(name)%2==0]

# Challege 1
numbers1 =  [1,1,2,3,5,8,13,21,34,55]
new_list6 = [number**2 for number in numbers1]
# Challenge 2
new_list7 = [number for number in numbers1 if number%2==0]


# Dictionary Comprehension 
#       new_dict = {new_key:new_value for item in item if test}
import random
new_dict1 = {name:random.randint(1,100) for name in names_list}

# new_dict = {new_key:new_value for (key,value) in dictionary.items() if test }
passed_students = {name:score for (name,score) in new_dict1.items() if score>60 }

#challenge 3
sentence = "What is Airspeed Velocity of an Unladen Swallow?"
new_dict2 = {word:len(word) for word in sentence.split()}

#challenge 4
weather_in_c = {
    "Monday":12,
    "Tuesday":14,
    "Wednesday":15,
    "Thrusday":14,
    "Friday":21,
    "Saturday":22,
    "Sunday":24,
}
new_dict3 = {day:temp* 9/5 +32 for (day,temp) in weather_in_c.items()}

print(new_dict3)



