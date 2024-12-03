import time

time1 = time.perf_counter()

input = open("inputs/day2.txt", "r")

def safeFun(report):
    # Working out if safe 
    # Checking for ascending or descending

    ascOrDesc = False

    if report == sorted(report):
        ascOrDesc = True
    elif report == sorted(report, reverse = True):
        ascOrDesc = True

    # Checking if any gaps are too big

    gapSafe = True
    for i in range(1, len(report)):
        diff = abs(report[i] - report[i-1])
        if diff < 1 or diff > 3:
            gapSafe = False

    # Works out if safe

    isSafe = False

    if ascOrDesc == True and gapSafe == True:
        isSafe = True
    
    return(isSafe)

safeCount = 0

for line in input:

    # Parsing inputs
    report = line.split()

    report = list(map(int, report))

    # Works out if safe

    alreadySafe = safeFun(report)
    
    if alreadySafe == True:
        safeCount += 1
    
    # Checks if problem damper will help
    
    else:
        becomesSafe = False

        for i in range(0, (len(report))):

            # Creates a temporary duplicate of the report

            testReport = report.copy()

            # Deletes the current level in the report

            testReport.pop(i)

            # Runs the test again to check if this new report is safe
            # If it is, updates the becomesSafe variable

            if safeFun(testReport) == True:
                becomesSafe = True
                break

        # Adds one to the safe counter if it becomes safe

        if becomesSafe == True:
            safeCount += 1

input.close()
print(safeCount)

time2 = time.perf_counter()

print(str(time2 - time1) + " seconds")