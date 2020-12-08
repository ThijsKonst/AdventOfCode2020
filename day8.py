import time

file1 = open('day8data')
lines = file1.readlines()

tic = time.perf_counter()
accumulator = 0
visitedLines = []
i = 0
jmplist = []
noplist = []
while i < len(lines):
    if i in visitedLines:
        break
    visitedLines.append(i)
    instruction, value = lines[i].split()
    if instruction == "jmp":
        jmplist.append(i)
        i += int(value)
    elif instruction == "acc":
        accumulator += int(value)
        i += 1
    else:
        noplist.append(i)
        i += 1
toc = time.perf_counter()
print(f"time it took: {toc - tic:0.4f} seconds")

for changes in jmplist:
    accumulator = 0
    visitedLines = []
    i = 0
    while i < len(lines):
        if i in visitedLines:
            break
        visitedLines.append(i)
        instruction, value = lines[i].split()
        if i == changes:
            instruction = "nop"

        if instruction == "jmp":
            i += int(value)
        elif instruction == "acc":
            accumulator += int(value)
            i += 1
        else:
            i += 1
        if i >= len(lines):
            print(i)
            print(accumulator, "lmao")
            break
