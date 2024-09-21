from tkinter import *
import math

WORK = 25
SHORT_BREAK = 5
LONG_BREAK = 20
REPS = 0
timer = None

window = Tk()
window.title("P O M O D O R O")
window.config(padx=20,pady=5,bg="black")


# timer/focus/rest label
label = Label(text="Timer",font=("times new roman",70,"bold"),bg="black",fg="#D1E9F6",padx=5,pady=5)
label.grid(row=0,column=1)

# count down mechanism
def countdown(count):
    global timer
    minu = math.floor(count/60)
    seco = count%60
    if seco < 10:
        seco = f"0{seco}"
    canva.itemconfig(text1, text=f"{minu}:{seco}")
    if count > 0:
        timer = window.after(1000,countdown,count-1)
    else:
        start()
        marks = ""
        session = math.floor(REPS/2)
        for _ in range(session):
            marks += "✅"
        tick_label.config(text=marks)
# Associating countdown with start button
def start():
    global REPS
    REPS += 1
    work_time  = WORK*60
    shortbreak_time = SHORT_BREAK*60
    longbreak_time = LONG_BREAK*60

    if (REPS%8==0):
        countdown(longbreak_time)
        label.config(text="BREAK !! ",fg="red")
        
    elif(REPS%2 == 0):
        countdown(shortbreak_time)
        label.config(text="BREAK !! ",fg="yellow")

    else:
        countdown(work_time)
        label.config(text="WORK !! ",fg="#6EC207")



#canvas creation
canva = Canvas(height=632,width=632,bg="black",highlightthickness=0)
tomato_image = PhotoImage(file="tomato.png")
canva.create_image(300,300,image = tomato_image)
canva.grid(row=1,column=1)
text1 = canva.create_text(300,325,text="00:00",fill="black",font=("times new roman",60,"bold"))


# Start Button Creation
start_button = Button(text="Start",font=("times new roman",30,"bold"),highlightthickness=0,padx=5,pady=5,command=start)
start_button.grid(row=2,column=0)

# Reset Button

def reset():
    window.after_cancel(timer)
    canva.itemconfig(text1,text ="00:00")
    label.config(text="Timer")
    tick_label.config(text="")
    global REPS
    REPS = 0



reset_button = Button(text="Reset",font=("times new roman",30,"bold"),highlightthickness=0,padx=5,pady=5,command=reset)
reset_button.grid(row=2,column=2)

# progess Tick_mark Label
tick_label = Label(bg="black",padx=2,pady=2)
tick_label.grid(row=2,column=1)
window.mainloop()


