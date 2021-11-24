from tkinter import *

root = Tk()
root.title("Kalkulusz")
height = 600
width = 400
root.resizable(width=False, height=False)


e = Entry(root, width=35, borderwidth=5)
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)


class Calculator:

    def __init__(self):
        self.f_num = None
        self.math = None
    
    @classmethod
    def button_click(number, self):
        current = e.get()
        e.delete(0, END)
        e.insert(0, str(current) + str(number))

    @classmethod
    def button_clear(self):
        e.delete(0, END)

    @classmethod
    def button_add(self):
        first_number = e.get()
        self.math = "add"
        self.f_num = int(first_number)
        e.delete(0, END)
    
    @classmethod
    def button_equal(self):
        second_number = e.get()
        e.delete(0, END)

        if self.math == "add":
            e.insert(0, self.f_num + int(second_number))

        if self.math == "subtract":
            e.insert(0, self.f_num - int(second_number))

        if self.math == "multiply":
            e.insert(0, self.f_num * int(second_number))

        if self.math == "divide":
            e.insert(0, self.f_num / int(second_number))

    @classmethod
    def button_subtract(self):
        first_number = e.get()
        self.math = "subtract"
        self.f_num = int(first_number)
        e.delete(0, END)

    @classmethod
    def button_multiply(self):
        first_number = e.get()
        self.math = "multiply"
        self.f_num = int(first_number)
        e.delete(0, END)

    @classmethod
    def button_divide(self):
        first_number = e.get()
        self.math = "divide"
        self.f_num = int(first_number)
        e.delete(0, END)


    button_1 = Button(root, text="1", padx=40, pady=20, command=lambda: Calculator.button_click(1))
    button_2 = Button(root, text="2", padx=40, pady=20, command=lambda: Calculator.button_click(2))
    button_3 = Button(root, text="3", padx=40, pady=20, command=lambda: Calculator.button_click(3))
    button_4 = Button(root, text="4", padx=40, pady=20, command=lambda: Calculator.button_click(4))
    button_5 = Button(root, text="5", padx=40, pady=20, command=lambda: Calculator.button_click(5))
    button_6 = Button(root, text="6", padx=40, pady=20, command=lambda: Calculator.button_click(6))
    button_7 = Button(root, text="7", padx=40, pady=20, command=lambda: Calculator.button_click(7))
    button_8 = Button(root, text="8", padx=40, pady=20, command=lambda: Calculator.button_click(8))
    button_9 = Button(root, text="9", padx=40, pady=20, command=lambda: Calculator.button_click(9))
    button_0 = Button(root, text="0", padx=40, pady=20, command=lambda: Calculator.button_click(0))
    
    button_add = Button(root, text="+", padx=39, pady=20, command=button_add)
    button_equal = Button(root, text="=", padx=88, pady=20, command=button_equal)
    button_clear = Button(root, text="Clear", padx=78, pady=20, command=button_clear)
    button_subtract = Button(root, text="-", padx=40, pady=20, command=button_subtract)
    button_multiply = Button(root, text="*", padx=40, pady=20, command=button_multiply)
    button_divide = Button(root, text="/", padx=40, pady=20, command=button_divide)


    button_1.grid(row=3, column=0)
    button_2.grid(row=3, column=1)
    button_3.grid(row=3, column=2)

    button_4.grid(row=2, column=0)
    button_5.grid(row=2, column=1)
    button_6.grid(row=2, column=2)

    button_7.grid(row=1, column=0)
    button_8.grid(row=1, column=1)
    button_9.grid(row=1, column=2)

    button_0.grid(row=4, column=0)
    button_add.grid(row=5, column=0)
    button_clear.grid(row=4, column=1, columnspan=2)
    button_equal.grid(row=5, column=1, columnspan=2)

    button_subtract.grid(row=6, column=0)
    button_multiply.grid(row=6, column=1)
    button_divide.grid(row=6, column=2)

root.mainloop()