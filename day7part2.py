def recursivesearch(rules, term):
    result = 1
    for color in rules[term]:
        result += color[1] * recursivesearch(rules, color[0])
    return result


file1 = open("day7data")
lines = file1.readlines()

rules = {}
for line in lines:
    line = line.split(" ")
    colors = []
    first = False
    for i in range(len(line)):

        if "bag" in line[i]:
            if first is False:
                first = line[i-2] + line[i-1]
            elif not line[i-2] == "no":
                colors.append(((line[i-2] + line[i-1]), int(line[i-3])))
    rules[first] = colors

print(recursivesearch(rules, 'shiny gold'))
