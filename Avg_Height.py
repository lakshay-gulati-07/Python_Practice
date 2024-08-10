student_heights = input("input a list of height of student ").split()
print(student_heights)
lenght = 0
height_sum = 0
for student in student_heights:
  lenght +=1
  height_sum += int(student)
print(lenght)
print(height_sum)
avg = round(height_sum/lenght)
print(f"Average Height is {avg}")