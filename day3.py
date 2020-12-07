file1 = open('day3data', 'r')
lines = file1.readlines()

roadmap=[]
for line in lines:
    roadmap.append(line.split("\n")[0])

count3 = 0
index = 0
for layer in roadmap:
    if layer[index] == '#':
        count3 += 1
    index = (index + 3) % len(layer)

count1 = 0
index = 0
for layer in roadmap:
    if layer[index] == '#':
        count1 += 1
    index = (index + 1) % len(layer)

count5 = 0
index = 0
for layer in roadmap:
    if layer[index] == '#':
        count5 += 1
    index = (index + 5) % len(layer)

count7 = 0
index = 0
for layer in roadmap:
    if layer[index] == '#':
        count7 += 1
    index = (index + 7) % len(layer)

countweird = 0
index = 0
for layer in range(int(len(roadmap)/2)):
    if roadmap[layer*2][index] == '#':
        countweird += 1
    index = (index + 1) % len(roadmap[layer*2])

print(count3*count1*count5*count7*countweird)
    
