
# two1nine
# eightwothree
# abcone2threexyz
# xtwone3four
# 4nineeightseven2
# zoneight234
# 7pqrstsixteen

file = open("2023_day1_input.txt", "r")
lines = file.readlines()

totalForFile = 0
for line in lines:
    numbers = {
        "0": "0",
        "1": "1",
        "2": "2",
        "3": "3",
        "4": "4",
        "5": "5",
        "6": "6",
        "7": "7",
        "8": "8",
        "9": "9",
        "zero": "0",
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9",
    }

    min, max = len(line) + 1, -1
    minVal, maxVal = 0, 0
    for key, val in numbers.items():
        index = line.find(key)
        if index != -1 and index < min:
            min = index
            minVal = val
        index = line.rfind(key)
        if index != -1 and index > max:
            max = index
            maxVal = val
    print("digits for line {} {}".format(minVal, maxVal))
    sumOfLine = int(''.join([minVal, maxVal]))
    print("sum for line {}".format(sumOfLine))
    totalForFile = totalForFile + sumOfLine
print("sum for file {}".format(totalForFile))
