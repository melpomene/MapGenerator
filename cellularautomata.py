# coding=utf8
import random, sys, copy

def randTile(prob):
    rand = random.random()
    if rand > prob:
        return "#"
    else:
        return " "

def generateInitialMap(height, width, density):
    col = []
    for y in range(height):
        row = []
        for x in range(width):
            row.append(randTile(1 - density))
        col.append(row)
    return col

def smooth(cave, iterations):
    new_cave = copy.deepcopy(cave)
    for y in range(len(cave)):
        for x in range(len(cave[y])):
            if 4 < wallsOnTile(cave, x, y):
                new_cave[y][x] = "#"
            else:
                new_cave[y][x] = " "
    printMap(new_cave)
    print ""
    if iterations == 0:
        return new_cave
    else:
        return smooth(new_cave,iterations-1)

def wallsOnTile(cave, x, y):
    walls = 0
    for i in [y-1, y, y+1]:
        for j in [x-1, x, x+1]:
            if i >= 0 and j >= 0 and i < len(cave) and j < len(cave[0]) :
                if cave[i][j] == "#":
                    walls+=1
            else:
                walls+=1
    return walls

def printMap(cave):
    for y in cave:
        for x in y:
            sys.stdout.write(str(x))
        print ""

if __name__ == "__main__":

    cave = generateInitialMap(20,90, 0.45)
    print "First iteration"
    printMap(cave)
    print ""
    print "Smoothing the map"
    cave = smooth(cave, 1)
    printMap(cave)

