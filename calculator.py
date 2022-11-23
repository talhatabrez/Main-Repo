from tkinter import *
root = Tk()

equa = " "
equation = StringVar()
calculation = Label(root, textvariable= equation)
equation.set("Enter your operation: ")
calculation.grid(columnspan=4)

def btnPress(num):
    global equa
    equa = equa + str(num)
    equation.set(equa)

def EqualPress():
    global equa
    total = str(eval(equa))
    equation.set(total)
    equa = " "

def clear():
    global equa
    equa = " "
    equation.set(" ")

B0 = Button(root, text="0", command=lambda:btnPress(0))
B0.grid(row=4, column=2)

B1 = Button(root, text="1", command=lambda:btnPress(1))
B1.grid(row=1, column=1)

B2 = Button(root, text="2", command=lambda:btnPress(2))
B2.grid(row=1, column=2)

B3 = Button(root, text="3", command=lambda:btnPress(3))
B3.grid(row=1, column=3)

B4 = Button(root, text="4", command=lambda:btnPress(4))
B4.grid(row=2, column=1)

B5 = Button(root, text="5", command=lambda:btnPress(5))
B5.grid(row=2, column=2)

B6 = Button(root, text="6", command=lambda:btnPress(6))
B6.grid(row=2, column=3)

B7 = Button(root, text="7", command=lambda:btnPress(7))
B7.grid(row=3, column=1)

B8 = Button(root, text="8", command=lambda:btnPress(8))
B8.grid(row=3, column=2)

B9 = Button(root, text="9", command=lambda:btnPress(9))
B9.grid(row=3, column=3)

Add = Button(root, text="+", command=lambda:btnPress("+"))
Add.grid(row=1, column=4)

Minus = Button(root, text="-", command=lambda:btnPress("-"))
Minus.grid(row=2, column=4)

Multiply = Button(root, text="*", command=lambda:btnPress("*"))
Multiply.grid(row=3, column=4)

Division = Button(root, text="/", command=lambda:btnPress("/"))
Division.grid(row=4, column=4)

Equals = Button(root, text="=", command= EqualPress)
Equals.grid(row=4, column=3)

clr = Button(root, text="clr", command= clear)
clr.grid(row=4, column=1)

root.mainloop()
