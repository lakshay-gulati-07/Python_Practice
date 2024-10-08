# importing Libraries
from tkinter import *
import pandas
import random

window = Tk()
window.title("Flash Card")
window.config(padx=50,pady=50,bg="#B1DDC6")
def flip_card():
    canvas.itemconfig(title,text="English",fill ="white")
    canvas.itemconfig(word,text = f"{new_word["English"]}",fill = "white")
    canvas.itemconfig(card_background,image = back_image)


flip_timer = window.after(3000,func=flip_card)


# Reading From Csv and Updating data to dict format
try:
    data = pandas.read_csv(filepath_or_buffer="data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/french_words.csv")
    updated_data = original_data.to_dict(orient="records")
else:
    updated_data = data.to_dict(orient="records")
new_word = {}

# Function that Generates New words by selecting Randomly from updated_data dict
def next_word():
    global new_word,flip_timer
    window.after_cancel(flip_timer)
    new_word = random.choice(updated_data)
    canvas.itemconfig(title,text ="French",fill="black")
    canvas.itemconfig(word,text=f"{new_word["French"]}",fill="black")
    canvas.itemconfig(card_background,image = front_image)
    flip_timer = window.after(3000,func=flip_card)

def is_known():
    updated_data.remove(new_word)
    data = pandas.DataFrame(updated_data)
    data.to_csv("data/words_to_learn.csv",index=False)
    next_word()
 


canvas = Canvas(width=800,height=526)
front_image = PhotoImage(file="images/card_front.png")
back_image = PhotoImage(file="images/card_back.png")
card_background = canvas.create_image(400,263,image = front_image)
# fill black - to change color of text to black
title = canvas.create_text(400,150,text="Title",font=("Ariel",40,"italic"),fill="black")
word = canvas.create_text(400,263,text="Word",font=("Ariel",60,"bold"),fill="black")
canvas.config(bg="#B1DDC6",highlightthickness= 0)
canvas.grid(row=0,column=0,columnspan=2)

# Button (wrong Button)
wrong_image = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_image,highlightthickness=0,command=next_word)
wrong_button.grid(row=1,column=0)

# Button(right Button)
right_image = PhotoImage(file="images/right.png")
right_button = Button(image=right_image,highlightthickness=0,command=is_known)
right_button.grid(row=1,column=1)


next_word()



window.mainloop()