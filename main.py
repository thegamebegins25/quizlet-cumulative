def getall(fname):
    #opens the file with all the vocab
    file = open(fname+".txt", "r")
    allL = file.read().splitlines()
    #loop
    all = {}
    for i in allL:
        #turns the vocab into a dictionary
        split = i.split("	")
        print(split)
        all[split[0]] = split[1]
    return all


def com():
    #opens the file with the comm.
    file = open(r"new.txt", "r")
    lines = file.read().splitlines()

    #filters out extra lines
    lines = list(filter(("").__ne__, lines))
    print(lines)
    all = getall("all")
    final = ""
    for i in lines:
        add = i + " " + all[i] + "\n"
        final = final + add

    #adds to output file
    file = open(r"out.txt", "w")
    file.writelines(final)
    print("Go to out.txt")

com()