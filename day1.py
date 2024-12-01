input = open("inputs/day1.txt", "r")

col1 = []
col2 = []

# Makes the two columns into lists
for line in input:
    col1.append(int(line[:5]))
    col2.append(int(line[8:13]))

input.close()

# Orders the lists smallest to largest

col1.sort()
col2.sort()

# Works out the differences

diff = 0

for i in range(len(col1)):
    diff += abs(col1[i-1]-col2[i-1])

print(diff)

# Part 2
# Working out how many times each number in the first list appears in the second list

simScore = 0

for item in col1:
    appears = 0
    for item2 in col2:
        if item == item2:
            appears += 1
    simScore += item*appears

print(str(simScore))