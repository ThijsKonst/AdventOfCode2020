file1 = open("day7data")
lines = file1.readlines()

rules = {}
goal = []
for line in lines:
    line = line.split(" ")
    colors = []
    for i in range(len(line)):
        if "bag" in line[i]:
            colors.append(line[i-2] + line[i-1])
    rules[colors[0]] = colors[1:]
    if colors[0] == "shinygold":
        goal.append(colors[0])

change = True
while change:
    change = False
    for color in set(rules.keys()) - set(goal):
        for value in rules[color]:
            if value in goal:
                goal.append(color)
                print(goal)
                change = True

goal.remove("shinygold")
print(len(set(goal)), " ", len(rules.keys()))
