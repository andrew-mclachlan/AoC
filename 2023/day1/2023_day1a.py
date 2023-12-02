
# 1abc2
# pqr3stu8vwx
# a1b2c3d4e5f
# treb7uchet

file = open("2023_day1_input.txt", "r")
lines = file.readlines()

totalForFile = 0
for line in lines:
    digitsForLine = []
    for c in line:
        if c.isdigit():
            digitsForLine.append(c)
    print("digits for line {}".format(digitsForLine))
    sumOfLine = int(''.join([digitsForLine[0], digitsForLine[len(digitsForLine) - 1]]))
    print("sum for line {}".format(sumOfLine))
    totalForFile = totalForFile + sumOfLine
print("sum for file {}".format(totalForFile))
