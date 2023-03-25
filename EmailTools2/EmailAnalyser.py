from Debugger import DBG

def Analyse(emails):
    global _max
    found = []
    nfound = []
    _max = 0
    logger = open(file="logs/highest_logger.txt", mode="w")
    
    ## Filtered (No Occurences)
    for i in range(len(emails)):
        if(not(emails[i] in found)):
            found.append(emails[i])

                
    for i in range(len(found)):
        count = emails.count(found[i])
        ##print(count)
        nfound.append(count)
        
    for i in range(len(found)):
        if(nfound[i] > _max):
            _max = nfound[i] 
                     
    if(DBG.IsDebuggerOn):
        print("Best Email:", found[nfound.index(_max)])             
    
    logger.write(str(found[nfound.index(_max)]) + '\n')
    logger.flush()
    logger.close()       