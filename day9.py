file1 = open("day9data")
lines = file1.readlines()

entries = []

for line in lines:
    entries.append(int(line.split("\n")[0]))

answer = 0
i = 25
while i < len(entries):
    valid = False
    for k in range(25):
        for j in [x for x in range(25) if x != k]:
            if entries[i - k - 1] + entries[i - j - 1] == entries[i]:
                valid = True
    if valid == False:
        print(entries[i])
        answer = entries[i]
        break

    i += 1

found = False
i = 2
while found == False:
    for j in range(len(entries)-i):
        answerArray = []
        for k in range(i):
            answerArray.append(entries[j+k])
        if sum(answerArray) == answer:
            print(sum(answerArray))
            print(min(answerArray) + max(answerArray))
            found = True
    i += 1

