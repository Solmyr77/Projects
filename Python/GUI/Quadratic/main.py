import math
from tkinter import *
from tkinter import ttk
from ttkbootstrap import Style


root = Tk()
root.title('Quadratic')
style = Style(theme='superhero')
root.resizable(width=False, height=False)
ttk_button = ttk.Button


e = Entry(root, width=35, borderwidth=5)
e.insert(0, 'Változók helye: ')


class Quadratic:


    def button_var_a_record():

        global a

        a = 0
        a = int(e.get())
        e.delete(0, END)


    def button_var_b_record():
        
        global b

        b = 0
        b = int(e.get())
        e.delete(0, END)


    def button_var_c_record():
        
        global c

        c = 0
        c = int(e.get())
        e.delete(0, END)


    def clear():

        e.delete(0, END)


    def x1():
        try:
            result_plus = (-b + math.sqrt(b*b - 4*a*c))/2*a
            rounded_result_plus = round(result_plus, 3)
            label_1.config(text=rounded_result_plus)
        except:
            label_1.config(text='Nincs eredmény')


    def x2():

        try:
            result_minus = (-b - math.sqrt(b*b - 4*a*c))/2*a
            rounded_result_minus = round(result_minus, 3)
            label_1.config(text=rounded_result_minus)
        except:
            label_1.config(text='Nincs eredmény')


button_1 = ttk_button(root, text="'A' változó felvétele", style='Outline.TButton', command=Quadratic.button_var_a_record)
button_2 = ttk_button(root, text="'B'Változó felvétele", style='Outline.TButton', command=Quadratic.button_var_b_record)
button_3 = ttk_button(root, text="'C'Változó felvétele", style='Outline.TButton', command=Quadratic.button_var_c_record)
button_4 = ttk_button(root, text="X,1", style='Outline.TButton', command=Quadratic.x1)
button_5 = ttk_button(root, text="X,2", style='Outline.TButton', command=Quadratic.x2)
button_6 = ttk_button(root, text="Clear", style='danger.Outline.TButton', command=Quadratic.clear)
label_1 = Label(root, text="")


e.grid(row=0, column=1, columnspan=1, padx=10, pady=10)
button_1.grid(row=1, column=0, padx=10, pady=10)
button_2.grid(row=1, column=1, padx=10, pady=10)
button_3.grid(row=1, column=2, padx=10, pady=10)
button_4.grid(row=3, column=0, padx=10, pady=10)
button_5.grid(row=3, column=2, padx=10, pady=10)
button_6.grid(row=0, column=0, padx=10, pady=10)
label_1.grid(row=3, column=1, padx=10, pady=10)


root.mainloop()
