'''
inputs for each function are :
    queue: contains the queue list of memory pages to load
    pageList: contains list of pages that are already in memory
    defaultLabel,pourcentageLabel:just lables for the simulation => simulator.py
    loadData:a function for load data in frames in the simulation => simulator.py
'''


def FIFO(queue,pageList,defaultLabel,pourcentageLabel,loadData):
    solution=[]
    defaultPage=0
    for i in range(len(pageList)):
        if len(queue)<4 and pageList[i] not in queue :
            queue.append(pageList[i])
            solution.append(pageList[i])
            defaultPage+=1
        else:
            if pageList[i] not in queue:
                page=queue.pop(0)
                solution[solution.index(page)]=pageList[i]
                queue.append(pageList[i])
                defaultPage+=1
        loadData(i,solution)
        
    defaultLabel.configure(text="page fault: {}".format(defaultPage))
    pourcentageLabel.configure(text="percentage of page fault: {}%".format(defaultPage*10)) 
 
#algorithme de remplacement des pages LRU         
def LRU(queue,pageList,defaultLabel,pourcentageLabel,loadData):
    solution=[]
    defaultPage=0
    for i in range(len(pageList)):
        if len(queue)<4 and pageList[i] not in queue:
            queue.append(pageList[i])
            defaultPage+=1
        else:
            if pageList[i] not in queue:
                #la recherche de la page victime
                page=victimLru(pageList[0:i],queue[:])
                queue[queue.index(page)]=pageList[i]
                defaultPage+=1
        loadData(i,queue)
        
    defaultLabel.configure(text="page fault: {}".format(defaultPage))
    pourcentageLabel.configure(text="percentage of page fault: {}%".format(defaultPage*10)) 
    
    
        
def victimLru(previousPages,queue):
    i=len(previousPages)-1
    while i>=0 and len(queue)!=1:
        if previousPages[i] in queue:
            queue.pop(queue.index(previousPages[i]))
        i-=1
            
    return queue[0]
             
        
        
                      
#algorithme de remplacement des pages OPTIMAL 
def OPTIMAL(queue,pageList,defaultLabel,pourcentageLabel,loadData):
    solution=[]
    defaultPage=0
    for i in range(len(pageList)):
        if len(queue)<4 and pageList[i] not in queue:
            queue.append(pageList[i])
            defaultPage+=1
        else:
            if pageList[i] not in queue:
                #la recherche de la page victime
                page=victimOptimal(pageList[i+1:],queue[:])
                queue[queue.index(page)]=pageList[i]
                defaultPage+=1
        loadData(i,queue)
        
    defaultLabel.configure(text="page fault: {}".format(defaultPage))
    pourcentageLabel.configure(text="percentage of page fault: {}%".format(defaultPage*10))

def victimOptimal(nextPages,queue):
    i=0
    while i<len(nextPages) and len(queue)!=1:
        if nextPages[i] in queue:
            queue.pop(queue.index(nextPages[i]))
        i+=1
            
    return queue[0]