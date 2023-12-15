from tkinter import *
from tkinter import ttk

def button_click(number):
    current = entry.get()
    entry.delete(0, END)
    entry.insert(0, str(current) + str(number))
    

def button_add():
    global math
    global f_num
    first_number = entry.get()
    entry.delete(0, END)
    math = "addition"
    f_num = float(first_number)

def button_subtract():
    global math
    global f_num
    first_number = entry.get()
    entry.delete(0, END)
    math = "subtraction"
    f_num = float(first_number)

def button_multiply():
    global math
    global f_num
    first_number = entry.get()
    entry.delete(0, END)
    math = "multiplication"
    f_num = float(first_number)

def button_divide():
    global math
    global f_num
    first_number = entry.get()
    entry.delete(0, END)
    math = "division"
    f_num = float(first_number)

def button_equal():
    second_number = entry.get()
    entry.delete(0, END)
    if math == "addition":
        entry.insert(0, f_num + float(second_number))
    elif math == "subtraction":
        entry.insert(0, f_num - float(second_number))
    elif math == "multiplication":
        entry.insert(0, f_num * float(second_number))
    elif math == "division":
        entry.insert(0, f_num / float(second_number))# other functions here

def button_clear():
    entry.delete(0, END)

def button_decimal():
    current = entry.get()
    if "." not in current:
        entry.insert(END, ".")

window = Tk()
window.title("Calculator")

style = ttk.Style()
style.configure("TButton", padding=(0, 5, 0, 5), font=('arial', 20, 'bold'))

entry = Entry(window, width=50, bd=8, font=('arial', 30, 'bold'))
entry.grid(row=0, column=0, columnspan=4)

button_1 = ttk.Button(window, text="1", style="TButton", width=10,command=lambda: button_click(1))
button_2 = ttk.Button(window, text="2", style="TButton", width=10,command=lambda: button_click(2))
button_3 = ttk.Button(window, text="3", style="TButton", width=10,command=lambda: button_click(3))
button_4 = ttk.Button(window, text="4", style="TButton", width=10,command=lambda: button_click(4))
button_5 = ttk.Button(window, text="5", style="TButton", width=10,command=lambda: button_click(5))
button_6 = ttk.Button(window, text="6", style="TButton", width=10,command=lambda: button_click(6))
button_7 = ttk.Button(window, text="7", style="TButton", width=10,command=lambda: button_click(7))
button_8 = ttk.Button(window, text="8", style="TButton", width=10,command=lambda: button_click(8))
button_9 = ttk.Button(window, text="9", style="TButton", width=10,command=lambda: button_click(9))
button_0 = ttk.Button(window, text="0", style="TButton", width=10,command=lambda: button_click(0))

button_add = ttk.Button(window, text="+", style="TButton", width=10,  command=button_add)
button_subtract = ttk.Button(window, text="-", style="TButton", width=10, command=button_subtract)
button_multiply = ttk.Button(window, text="*", style="TButton", width=10, command=button_multiply)
button_divide = ttk.Button(window, text="/", style="TButton", width=10,command=button_divide)
button_equal = ttk.Button(window, text="=", style="TButton", width=10, command=button_equal)

button_clear = ttk.Button(window, text="Clear", style="TButton", width=10, command=button_clear)

button_decimal = ttk.Button(window, text=".", style="TButton", width=10, command=button_decimal)

button_1.grid(row=5, column=0, sticky=NSEW)
button_2.grid(row=5, column=1, sticky=NSEW)
button_3.grid(row=5, column=2, sticky=NSEW)

button_4.grid(row=4, column=0, sticky=NSEW)
button_5.grid(row=4, column=1, sticky=NSEW)
button_6.grid(row=4, column=2, sticky=NSEW)

button_7.grid(row=3, column=0, sticky=NSEW)
button_8.grid(row=3, column=1, sticky=NSEW)
button_9.grid(row=3, column=2, sticky=NSEW)

button_0.grid(row=6, column=0, columnspan=2, sticky=NSEW)
button_add.grid(row=5, column=3, sticky=NSEW)
button_subtract.grid(row=4, column=3, sticky=NSEW)

button_multiply.grid(row=1, column=3, sticky=NSEW)
button_divide.grid(row=3, column=3, sticky=NSEW)
button_equal.grid(row=6, column=3, sticky=NSEW)

button_clear.grid(row=1, column=0, columnspan=3, sticky=NSEW)

button_decimal.grid(row=6, column=2, sticky=NSEW)

window.mainloop()
