file1 = open('day6data', 'r')
lines = file1.readlines()

total = []
group = False
count = 0
for line in lines:
    if line == "\n":
        print(group)

        count += len(group)
        group = False
    else:
       


        print(line)
        if group == False:
            group = line.split("\n")[0]
        else:
            group = [value for value in group if value in line]

count += len(group)
print(count)

