from datetime import datetime as dt
from time import time

def equation_logger(data):
    time = dt.now().strftime('%H:%M')
    with open('log.csv', 'a') as file:
        file.write('{};equation were inserted;{}\n'
                    .format(time, data))

def showRes_logger(data):
    time = dt.now().strftime('%H:%M')
    with open('log.csv', 'a') as file:
        file.write('{};show result of caculation;{}\n'
                    .format(time, data))

def calcPressed_logger():
    time = dt.now().strftime('%H:%M')
    with open('log.csv', 'a') as file:
        file.write('{};button "calculate were pressed"\n'
                    .format(time))

def exit_logger():
    time = dt.now().strftime('%H:%M')
    with open('log.csv', 'a') as file:
        file.write('{};exit from app\n'
                    .format(time))

