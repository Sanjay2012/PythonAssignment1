#Step1: Import tkinter package
from tkinter import *

#Step2: gui Interaction
window=Tk()
window.geometry("500x500")

#Step3: Adding inputs

    #Create entry box
e=Entry(window, width=56, borderwidth=5)
e.place(x=0, y=0)

    #Create buttons
    
def click(num):
    result=e.get()
    e.delete(0, END)
    e.insert(0, str(result) + str(num))
    
b=Button(window, text='1', width=12, command=lambda:click(1))
b.place(x=10, y=60)

b=Button(window, text='2', width=12, command=lambda:click(2))
b.place(x=80, y=60)

b=Button(window, text='3', width=12, command=lambda:click(3))
b.place(x=170, y=60)

b=Button(window, text='4', width=12, command=lambda:click(4))
b.place(x=10, y=120)

b=Button(window, text='5', width=12, command=lambda:click(5))
b.place(x=80, y=120)

b=Button(window, text='6', width=12, command=lambda:click(6))
b.place(x=170, y=120)

b=Button(window, text='7', width=12, command=lambda:click(7))
b.place(x=10, y=180)

b=Button(window, text='8', width=12, command=lambda:click(8))
b.place(x=80, y=180)

b=Button(window, text='9', width=12, command=lambda:click(9))
b.place(x=170, y=180)

b=Button(window, text='0', width=12, command=lambda:click(0))
b.place(x=10, y=240)

#Operators
## 1. addition function
def ADD():
    n1=e.get()
    global math
    math="addition"
    global i
    i=int(n1)
    e.delete(0, END)

b=Button(window, text='+', width=12, command=ADD)
b.place(x=80, y=240)

## 2. substraction function
def SUB():
    n1=e.get()
    global math
    math="substraction"
    global i
    i=int(n1)
    e.delete(0, END)

b=Button(window, text='-', width=12, command=SUB)
b.place(x=170, y=240)

## 3. multiplication function
def MUL():
    n1=e.get()
    global math
    math="multiplication"
    global i
    i=int(n1)
    e.delete(0, END)

b=Button(window, text='*', width=12, command=MUL)
b.place(x=10, y=300)

## 4. division function
def DIV():
    n1=e.get()
    global math
    math="division"
    global i
    i=int(n1)
    e.delete(0, END)

b=Button(window, text='/', width=12, command=DIV)
b.place(x=80, y=300)


## 5. modulus function
def MOD():
    n1=e.get()
    global math
    math="modulus"
    global i
    i=int(n1)
    e.delete(0, END)

b=Button(window, text='%', width=12, command=MOD)
b.place(x=170, y=300)


## 6. power function
def POW():
    n1=e.get()
    global math
    math="power"
    global i
    i=int(n1)
    e.delete(0, END)

b=Button(window, text='^', width=12, command=POW)
b.place(x=10, y=360)

## 7. Equal function
def EQUAL():
    n2=e.get()
    e.delete(0, END)
    if math=='addition':
        e.insert(0, i + int(n2))
    elif math=="substraction":
         e.insert(0, i - int(n2))
    elif math=="multiplication":
         e.insert(0, i * int(n2))
    elif math=="division":
         e.insert(0, i / int(n2))
    elif math=="modulus":
         e.insert(0, i % int(n2))
    elif math=="power":
         e.insert(0, i ** int(n2))

b=Button(window, text='=', width=12, command=EQUAL)
b.place(x=80, y=360)

## 8. Clear function
def CLEAR():
    e.delete(0, END)
    
b=Button(window, text='Clear', width=12, command=CLEAR)
b.place(x=170, y=360)

#Step4: Mainloop
mainloop()


