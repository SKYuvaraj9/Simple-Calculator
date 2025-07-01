import tkinter
from tkinter import *
import math
root=Tk()
root.title("CALSY WITH TASSU")
root.geometry("300x400")
root.resizable(False,False)
root.configure(bg="purple")

equation=""
def show(symbol):
    global equation
    equation+=symbol
    label_result.config(text=equation)

def clear():
    global equation
    equation=""
    label_result.config(text=equation)

def delete():
    global equation
    n=len(equation)-1
    equation=equation.replace(equation[n],"")
    label_result.config(text=equation)

def fact():
    global equation
    n=int(equation)
    mul=1
    for i in range(1,n+1,1):
        mul=mul*i
    equation=int(mul)
    label_result.config(text=equation)

def calculate():
    global equation
    result=""
    if equation !="":
        try:
            result=eval(equation)
            equation=str(result)
        except:
            result="error"
            equation=""
    label_result.config(text=result)


label_result=Label(root,width=200,height=4,text="",font=("arial",15),fg="black",bg="pink")
label_result.pack()

Button(root,text="C",width=6,height=2,font=("arial",10,"bold"),bd=1,fg="black",bg="slateblue",command=lambda: clear()).place(x=10,y=110)
Button(root,text="del",width=6,height=2,font=("arial",10,"bold"),bd=1,fg="black",bg="slateblue",command=lambda: delete()).place(x=85,y=110)
Button(root,text="!",width=6,height=2,font=("arial",10,"bold"),bd=1,fg="black",bg="deeppink",command=lambda: fact()).place(x=160,y=110)
Button(root,text="*",width=6,height=2,font=("arial",10,"bold"),bd=1,fg="black",bg="deeppink",command=lambda: show("*")).place(x=235,y=110)

Button(root,text="7",width=6,height=2,font=("arial",10,"bold"),bd=1,fg="black",bg="crimson",command=lambda: show("7")).place(x=10,y=170)
Button(root,text="8",width=6,height=2,font=("arial",10,"bold"),bd=1,fg="black",bg="crimson",command=lambda: show("8")).place(x=85,y=170)
Button(root,text="9",width=6,height=2,font=("arial",10,"bold"),bd=1,fg="black",bg="crimson",command=lambda: show("9")).place(x=160,y=170)
Button(root,text="-",width=6,height=2,font=("arial",10,"bold"),bd=1,fg="black",bg="deeppink",command=lambda: show("-")).place(x=235,y=170)

Button(root,text="4",width=6,height=2,font=("arial",10,"bold"),bd=1,fg="black",bg="crimson",command=lambda: show("4")).place(x=10,y=230)
Button(root,text="5",width=6,height=2,font=("arial",10,"bold"),bd=1,fg="black",bg="crimson",command=lambda: show("5")).place(x=85,y=230)
Button(root,text="6",width=6,height=2,font=("arial",10,"bold"),bd=1,fg="black",bg="crimson",command=lambda: show("6")).place(x=160,y=230)
Button(root,text="+",width=6,height=2,font=("arial",10,"bold"),bd=1,fg="black",bg="deeppink",command=lambda: show("+")).place(x=235,y=230)

Button(root,text="3",width=6,height=2,font=("arial",10,"bold"),bd=1,fg="black",bg="crimson",command=lambda: show("3")).place(x=10,y=290)
Button(root,text="2",width=6,height=2,font=("arial",10,"bold"),bd=1,fg="black",bg="crimson",command=lambda: show("2")).place(x=85,y=290)
Button(root,text="1",width=6,height=2,font=("arial",10,"bold"),bd=1,fg="black",bg="crimson",command=lambda: show("1")).place(x=160,y=290)
Button(root,text="/",width=6,height=2,font=("arial",10,"bold"),bd=1,fg="black",bg="deeppink",command=lambda: show("/")).place(x=235,y=290)

Button(root,text="0",width=15,height=2,font=("arial",10,"bold"),bd=1,fg="black",bg="crimson",command=lambda: show("0")).place(x=10,y=350)
Button(root,text=".",width=6,height=2,font=("arial",10,"bold"),bd=1,fg="black",bg="pink",command=lambda: show(".")).place(x=160,y=350)

Button(root,text="=",width=6,height=2,font=("arial",10,"bold"),bd=1,fg="black",bg="indigo",command=lambda: calculate()).place(x=235,y=350)

root.mainloop()


