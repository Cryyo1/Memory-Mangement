import tkinter as tk
import random
from algorithm import FIFO,LRU,OPTIMAL


#fill the list of page in the queue 
pageList=[random.randint(1,9) for i in range(10)]
print(pageList)
#what containts memory
queue=[]
#frame represenation
memory={}
#statistics
defaultLabel=None
pourcentageLabel=None 
pageInput=None
 

#print the content of memory each time a page is loaded 
def loadData(i,solution):
    for j in range(4):
        if j<len(solution):
            memory[(j+1,i+1)].configure(text=str(solution[j]))
            
    
#Reset of all widget function
def Reset():
    #clear the queue of memory
    global queue
    queue.clear() 

    for ligne in range(1,5):
        for colonne in range(1,11):
             memory[(ligne,colonne)].configure(text="")

#new example
def randomExample():
    Reset()
    global pageList
    pageList=[random.randint(1,9) for i in range(10)]
    
    for i in range(10):
        memory[0,i+1].configure(text="{}".format(pageList[i]))
        
#manual example
def OK():
    global pageList
    pageList=pageInput.get(1.0,tk.END).replace(' ', '').split(',')
    pageList=[int(pageList[i]) for i in range(len(pageList))]
    for i in range(10):
        memory[0,i+1].configure(text="{}".format(pageList[i]))
    
    
            


#Création of  main window
#buttons to represent memory frames
#inputs to enter page list manuall
#command buttons for running the 3 algorithms

window = tk.Tk()
window.title("Memory simulator")
window.configure(height=400,width=800)
window.minsize(800, 400)




frame = tk.Frame(window)
frame.configure(height=250,width=550)
frame.place(x=50,y=50)


for ligne in range(5):
     for colonne in range(11):
        button=tk.Button(frame, text='',borderwidth=1,width=6,height=2)
        button.grid(row=ligne, column=colonne)
        if colonne == 0 and ligne > 0:
            button.configure(text="page {}".format(ligne),bg='grey')
        elif colonne > 0 and ligne == 0:
            button.configure(text="{}".format(pageList[colonne-1]),bg='grey')
           
        memory[(ligne,colonne)]=button
            

label=tk.Label(text="Enter a custom page list :")
label.place(x=100,y=25)

pageInput = tk.Text(window, height = 1,width = 40,bg = "light yellow")
pageInput.place(x=230,y=25)

ok=tk.Button(window, text='Ok',width=4,height=1,command=OK)
ok.place(x=560,y=22)

fifoButton=tk.Button(window, text='FIFO',width=8,height=2,command= lambda: FIFO(queue,pageList,defaultLabel,pourcentageLabel,loadData))
fifoButton.place(x=650,y=50)

lruButton=tk.Button(window, text='LRU',width=8,height=2,command= lambda: LRU(queue,pageList,defaultLabel,pourcentageLabel,loadData))
lruButton.place(x=650,y=100)

optiamlButton=tk.Button(window, text='OPTIMAL',width=8,height=2,command= lambda: OPTIMAL(queue,pageList,defaultLabel,pourcentageLabel,loadData))
optiamlButton.place(x=650,y=150)

reset=tk.Button(window, text='Reset',width=8,height=2,command=Reset)
reset.place(x=650,y=200)

randomexample=tk.Button(window, text='new example',width=12,height=2,command=randomExample)
randomexample.place(x=650,y=250)

defaultLabel=tk.Label()
defaultLabel.place(x=200,y=270)
pourcentageLabel=tk.Label() 
pourcentageLabel.place(x=200,y=300)      
        
window.mainloop()