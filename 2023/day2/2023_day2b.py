
# Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
# Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
# Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
# Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
# Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green
# 
# 12 red cubes, 13 green cubes, and 14 blue cubes

file = open("2023_day2_input.txt", "r")
lines = file.readlines()

totalForFile = 0
for line in lines:
    game = line.strip().split(':')
    id = int(game[0][5:])
    reveal = game[1].strip().split(';')
    print("line {} {}".format(game, reveal))
    maxR, maxG, maxB = 0, 0, 0
    for bag in reveal:
        colours = bag.strip().split(",")
        red, green, blue = 0, 0, 0
        for colour in colours:
            value = colour.strip().split(" ")
            if value[1] == "red":
                red = int(value[0])
            elif value[1] == "green":
                green = int(value[0])
            elif value[1] == "blue":
                blue = int(value[0])
        if red > maxR:
            maxR = red
        if green > maxG:
            maxG = green
        if blue > maxB:
            maxB = blue
    print("{} {} {}".format( maxR, maxG, maxB))
    power = maxR * maxG * maxB
    totalForFile += power
print("sum for file {}".format(totalForFile))
