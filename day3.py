import re
input = open("inputs/day3.txt")

cleanedInput = []
do = True

# Pulls out all the mul phrases according to whether they are or are not needed

for line in input:
    splitLine = re.split("(don't|do)", line)

    for item in splitLine:

        if item == "don't":
            do = False
        elif item == "do":
            do = True
        
        if do == True:
            cleanedInput.extend(re.findall("mul\([0123456789]+,[0123456789]+\)", item))

input.close()

numbers = []

# Pulls out just the numbers

for item in cleanedInput:
    numbers.extend(re.findall("[0123456789]+", item))

total = 0

# Multiplies adjacent numbers and adds them to the total

for i in range(0, len(numbers), 2):
    total += int(numbers[i]) * int(numbers[i + 1])

print(total)