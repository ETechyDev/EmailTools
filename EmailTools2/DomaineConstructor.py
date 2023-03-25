from random import choice
def Construct():
    domaineData = ["gmail", "outlook", "yahoo"]
    domaine = choice(domaineData)
    return "@" + domaine + ".com"


def ConstructCopies(n, name):
    domaines = [] 
    logger = open(file="logs/domaine_log.txt", mode="w")
    for i in range(n):
        domaine = Construct()
        logger.write((name + domaine) + '\n')
        domaines.append(name + domaine)
    logger.flush()
    logger.close()
    return domaines