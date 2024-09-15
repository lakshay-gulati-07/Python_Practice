import tkinter
window = tkinter.Tk()
window.minsize(width=500,height=200)
window.title("Miles to Km Converter TKinter")

# Input 
input = tkinter.Entry(width=7)
input.grid(column=1,row=0,padx=5,pady=5)

# Miles Label
miles_label = tkinter.Label(text="Miles")
miles_label.grid(column=2,row=0,padx=5,pady=5)

# is_equal Label
iqt = tkinter.Label(text="is Equal to - ")
iqt.grid(column=0,row=1,padx=5,pady=5)

# Result Calculation 
result_label = tkinter.Label(text="0")
result_label.grid(column=1,row=1,padx=5,pady=5)


def cal():
    miles = input.get()
    km = float(miles) * 1.609
    result_label.config(text=f"{km}")


# Km Label 
km_label = tkinter.Label(text ="Km")
km_label.grid(row=1,column=2,padx=5,pady=5)

# calculate Button
button = tkinter.Button(text="Calculate",command=cal)
button.grid(row=2,column=1,padx=5,pady=5)



window.mainloop()