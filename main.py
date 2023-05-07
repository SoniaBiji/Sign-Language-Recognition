from tkinter import *  
from tkinter import ttk
import predict as pr
import collect as col
import train as trn
#creating the application main window.   
window = Tk() 
window.geometry("350x250")  
window.resizable(False, False)
global entry
def collection():
    def runcollection():
        res= entry.get()
        col.runcollection(res)
        
    label=Label(window, text="Enter a word to train", font=("Courier 10 bold"))
    label.pack()
    entry= Entry(window, width= 40)
    entry.focus_set()
    entry.pack()
    btn = Button(window, text = "Next", fg = "green",command=runcollection).place(x = 200,y = 50) 
    
    
def training():
    trn.runTrain()
def prediction():
    pr.runPrediction()
#Entering the event main loop
collect = Button(window, text = "Collect Data", fg = "blue",command=collection).place(x = 100,y = 100) 

train = Button(window, text = "Train Data ", fg = "blue",command=training).place(x = 100,y = 150)  
   
predict = Button(window, text = "Predict Data", fg = "blue",command=prediction).place(x = 100,y = 200)  
   
window.mainloop()  