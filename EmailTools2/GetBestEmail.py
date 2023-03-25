def Filter(path):
    file = open(file=path, mode="r")
    email_unfiltered = file.read()
    email_filtered = ""
    for i in email_unfiltered:
        if(i.isalpha() or i.isdigit()):
            email_filtered += i
    file.flush()
    file.close()
    return email_filtered