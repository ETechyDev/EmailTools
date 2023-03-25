from Debugger import DBG 

def Analyse(domaines):
    global _max
    found = []
    nfound = []
    _max = 0
    logger = open(file="logs/highest_domaine_log.txt", mode="w")
    
    ## Filtered (No Occurences)
    for i in range(len(domaines)):
        if(not(domaines[i] in found)):
            found.append(domaines[i])
    
    for i in range(len(found)):
        count = domaines.count(found[i])
        nfound.append(count)
    
    for i in range(len(nfound)):
        if(nfound[i] > _max):
            _max = nfound[i]
    
    if(DBG.IsDebuggerOn == True):
        print("Best Domaine:", found[nfound.index(_max)]) 
    
    logger.write(str(found[nfound.index(_max)]) + '\n')
    logger.flush()
    logger.close()