import tkinter as tk

calculationText = ""

def buttonPress(theButton):
    global calculationText
    calculationText = calculationText + str(theButton)
    equation.set(calculationText)


def equalPress():
    try:
        global calculationText
        total = str(eval(calculationText))
        equation.set(total)
        calculationText=""
    except:
        equation.set("error")
        calculationText = ""

def cPress():
    global calculationText
    calculationText = ""
    equation.set("")

def backspacePress():
    global calculationText
    if calculationText != "":
        calculationText = calculationText[:-1]
        equation.set(calculationText)
    else:
        pass


if __name__ == "__main__":



    window = tk.Tk()
    window.title("Basic Calculator")
    equation = tk.StringVar()


    calculation = tk.Label(master=window,textvariable=equation,width=40, height=5)
    calculation.grid(row=0, column=0, columnspan=4)


    buttonPlus = tk.Button(text="+", width=10, height=5,command=lambda:buttonPress('+'))
    buttonPlus.grid(row=5,column=3)
    buttonMinus = tk.Button(text="-",width=10,height=5,command=lambda:buttonPress('-'))
    buttonMinus.grid(row=4,column=3)
    buttonDivide = tk.Button(text="/",width=10,height=5,command=lambda:buttonPress('/'))
    buttonDivide.grid(row=2,column=3)
    buttonMultiply = tk.Button(text="*",width=10,height=5,command=lambda:buttonPress('*'))
    buttonMultiply.grid(row=3,column=3)
    buttonEquals = tk.Button(text="=",width=10,height=5,command=lambda:equalPress())
    buttonEquals.grid(row=6,column=3)
    buttonBackspace = tk.Button(text="<-",width=10,height=5,command=lambda:backspacePress())
    buttonBackspace.grid(row=1,column=3)
    buttonC = tk.Button(text="C",width=10,height=5,command=lambda:cPress())
    buttonC.grid(row=1,column=2)
    buttonZero = tk.Button(text="0",width=10,height=5,command=lambda:buttonPress('0'))
    buttonZero.grid(row=6,column=1)
    buttonOne = tk.Button(text="1",width=10,height=5,command=lambda:buttonPress('1'))
    buttonOne.grid(row=5,column=0)
    buttonTwo = tk.Button(text="2",width=10,height=5,command=lambda:buttonPress('2'))
    buttonTwo.grid(row=5,column=1)
    buttonThree = tk.Button(text="3",width=10,height=5,command=lambda:buttonPress('3'))
    buttonThree.grid(row=5,column=2)
    buttonFour = tk.Button(text="4",width=10,height=5,command=lambda:buttonPress('4'))
    buttonFour.grid(row=4,column=0)
    buttonFive = tk.Button(text="5",width=10,height=5,command=lambda:buttonPress('5'))
    buttonFive.grid(row=4,column=1)
    buttonSix = tk.Button(text="6",width=10,height=5,command=lambda:buttonPress('6'))
    buttonSix.grid(row=4,column=2)
    buttonSeven = tk.Button(text="7",width=10,height=5,command=lambda:buttonPress('7'))
    buttonSeven.grid(row=3,column=0)
    buttonEight = tk.Button(text="8",width=10,height=5,command=lambda:buttonPress('8'))
    buttonEight.grid(row=3,column=1)
    buttonNine = tk.Button(text="9",width=10,height=5,command=lambda:buttonPress('9'))
    buttonNine.grid(row=3,column=2)
    buttonDot = tk.Button(text=".",width=10,heigh=5,command=lambda:buttonPress('.'))
    buttonDot.grid(row=6,column=2)





    # add more buttons
    buttonX1 = tk.Button(text="TAN",width=10,height=5,)
    buttonX1.grid(row=2,column=2)
    buttonX2 = tk.Button(text="SIN",width=10,height=5,)
    buttonX2.grid(row=2,column=1)
    buttonX3 = tk.Button(text="LOG",width=10,height=5,)
    buttonX3.grid(row=1,column=1)
    buttonX4 = tk.Button(text="COS",width=10,height=5,)
    buttonX4.grid(row=2,column=0)
    buttonX5 = tk.Button(text="ROOT",width=10,height=5,)
    buttonX5.grid(row=1,column=0)

    window.mainloop()  # keeps the window open