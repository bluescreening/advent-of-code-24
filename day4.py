file = open("inputs/day4.txt", "r")

input = file.read().splitlines()

file.close()

changeCoOrds = [[1,0],[0,1],[1,1],[-1,0],[0,-1],[-1,-1],[-1,1],[1,-1]]

def movingAround(iteration):

    xmasCount = 0

    x = 0
    y = 0
    dy = changeCoOrds[iteration][1]
    dx = changeCoOrds[iteration][0]

    for y in range(len(input)):

        for x in range(len(input[0])):

            if (x + 3*dx >= len(input) or x + 3*dx < 0) or (y + 3*dy >= len(input) or y + 3*dy < 0):
                continue

            fourLetters = input[y][x] + input[y + dy][x + dx] + input[y + 2*dy][x + 2*dx] + input[y + 3*dy][x + 3*dx]

            if fourLetters == "XMAS":
                xmasCount += 1

    return(xmasCount)


crossCount = 0

for y in range(len(input)-2):

    for x in range(len(input[0])-2):

        cross = input[y][x] + input[y+1][x+1] + input[y+2][x+2] + input[y][x+2] + input[y+2][x]

        if cross == "MASSM" or cross == "MASMS" or cross == "SAMSM" or cross == "SAMMS":
            crossCount += 1

xmasTotal = 0

for i in range(0,8):
    xmasTotal += movingAround(i)

print(xmasTotal)
print(crossCount)