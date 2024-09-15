import tkinter 
window = tkinter.Tk()
window.title("First GUI")
window.minsize(width=500,height=300)
label1 = tkinter.Label(text = "First Label")
label1.pack()

# Challenge 1 Method with Unlimided Argument

def add(*args):
    sum = 0
    print(args)
    print(args[0])
    for n in args:
        sum += n
    print(sum)

# Challenge 2 kwargs Keyword Arguments
def calculator(**kwargs):
    print(kwargs)
    for (key,value) in kwargs.items():
        print(key)
        print(value)

add(2,2,2,2,2)
calculator(add=2,mul=4)

class car:
    def __init__(self,**kwargs):
        self.company = kwargs.get("company")
        self.model = kwargs.get("model")
    
my_car = car(company = "BMW")
print(my_car.company)


# TKinter Buttons,Entry etc.
def on_click():
    user_input = input.get()
    label1.config(text=user_input)


button = tkinter.Button(text="Click Me !!", command=on_click)
button.pack()

# Entry 
input = tkinter.Entry()
input.pack()






window.mainloop()