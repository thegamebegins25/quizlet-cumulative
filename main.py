file = open(r"new.txt", "r")
lines = file.read().splitlines()

lines = list(filter(("").__ne__, lines))
print(lines)

file = open(r"all.txt", "r")
allL = file.read().splitlines()

all = {}
for i in allL:
    split = i.split("	")
    print(split)
    all[split[0]] = split[1]
print(all)
final = ""
for i in lines:
    add = i + "	" + all[i] + "\n"
    final = final + add

file = open(r"out.txt", "w")
file.writelines(final)
    