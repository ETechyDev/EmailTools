from random import randint
def Construct(name):
    f = randint(20, 99)
    return name + str(f)

def ConstructCopies(n, name):
    emails = []
    logger = open(file="logs/email_log.txt", mode="w")
    for i in range(n):
        email = Construct(name)
        logger.write(email + '\n')
        emails.append(email)
    logger.flush()
    logger.close()
    return emails
