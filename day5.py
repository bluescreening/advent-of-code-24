# Parsing input

input = open("inputs/day5.txt", "r")

rules = []
pageLists = []
isRule = True

for line in input:
    if line.strip() == "":
        isRule = False
    elif isRule == True:
        rules.append(line.strip())
    else:
        pageLists.append(line.strip())

input.close()

for i in range(len(pageLists)):
    pageLists[i] = str(pageLists[i]).split(",")

# Working out if safe or not

safeManuals = []
swappedManuals = []

def check(listOfManuals):
    for manual in listOfManuals:
        triedSwap = False
        for page in manual:
            for rule in rules:
                index = rule.find(page)
                if index == -1 or index == 0 or (rule[0:2] in manual) == False:
                    continue
                elif manual.index(rule[0:2]) > manual.index(page):
                    triedSwap = True
                    experiment = manual.copy()
                    experiment[manual.index(page)] = manual[manual.index(rule[0:2])]
                    experiment[manual.index(rule[0:2])] = manual[manual.index(page)]
                    manual = experiment
        if triedSwap == False:
            safeManuals.append(manual)
        else:
            swappedManuals.append(manual)

check(pageLists)
print(swappedManuals)

safeTotal = 0
for manual in safeManuals:
    safeTotal += int(manual[int((len(manual)-1)/2)])

print("The number of manuals that were initially safe is " + str(safeTotal))

safeManuals = []

while len(swappedManuals) > 0:
    checkList = swappedManuals.copy()
    swappedManuals = []
    check(checkList)

safeTotal = 0
for manual in safeManuals:
    safeTotal += int(manual[int((len(manual)-1)/2)])

print("The number of manuals that became safe is " + str(safeTotal))