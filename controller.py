import model_calc as model
import view_calc as view
import threading
import time


def startProgr():
    e1 = threading.Thread(target=calculate)
    e1.start()
    e1.isDaemon()
    view.initWindow()

def calculate():
    while(view.isExit!=True):      
        while(view.isPressedCalc!=True):  
            if(view.isExit):
                exit() 
            time.sleep(2)              
        eq = str(view.getEquation())
        model.initEquation(eq)
        result=model.calculate()
        view.showResult(result)
    

