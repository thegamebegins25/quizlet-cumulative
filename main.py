#opens the file with the comm.
file = open(r"new.txt", "r")
lines = file.read().splitlines()

#filters out extra lines
lines = list(filter(("").__ne__, lines))
print(lines)

#opens the file with all the vocab
file = open(r"all.txt", "r")
allL = file.read().splitlines()
#loop
all = {}
for i in allL:
    #turns the vocab into a dictionary
    split = i.split("	")
    print(split)
    all[split[0]] = split[1]
print(all)
#gets the def of the terms in the comm. list
final = ""
for i in lines:
    add = i + "\g" + all[i] + "\n"
    final = final + add

#adds to output file
file = open(r"out.txt", "w")
file.writelines(final)
    