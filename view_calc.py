import tkinter as tk
from tkinter import *
from tkinter import messagebox
import logger as log

equation_tf=Entry()
calc_btn =Button()
isPressedCalc=False
isExit=False
window = Tk()

def initWindow():        
    window.title("Калькулятор")
    window.geometry('400x300')
    global equation_tf
    global calc_btn

    frame = Frame(window)
    frame.pack(expand=True)

    equation_lb =Label(frame,text="Введите уравнение для расчета")
    equation_lb.grid(row=3, column=1)
 
    equation_tf=Entry(frame,)
    equation_tf.grid(row=3, column=2)


    exit_btn=Button(frame,text="Выйти",command=exit)
    exit_btn.grid(row=5, column=2)

    calc_btn=Button(frame,text="Расчитать",command=keyPressed)
    calc_btn.grid(row=4, column=2, padx=10, pady=10)
    window.mainloop()

def getEquation():
    eq=str(equation_tf.get())
    log.equation_logger(eq)
    return eq

def showResult(result):
    global isPressedCalc
    isPressedCalc=False
    log.showRes_logger(result)
    messagebox.showinfo("Результат вычислений: ", result)

def keyPressed():
    global isPressedCalc
    isPressedCalc=True
    log.calcPressed_logger()
    
def exit():
    global isExit
    isExit=True
    log.exit_logger()
    window.destroy()

