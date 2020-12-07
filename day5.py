file1 = open("day5data", 'r')
lines = file1.readlines()

maximal = 0
idlist = []
for line in lines:
    row = line[:7]
    rownumber = 0
    column = line [7:]
    colnumber = 0

    for i in range(7):
        if row[6-i] == 'B':
            rownumber += 2 ** i

    for i in range(3):
        if column[2-i] == 'R':
            colnumber += 2 ** i
    seatid = rownumber*8+colnumber
    idlist.append(seatid)
    if seatid > maximal:
        maximal = seatid 


print(maximal)

idlist.sort()
print(idlist)

for entry in idlist:
    if (not (entry + 1) in idlist) and ((entry + 2) in idlist):
        print(entry + 1)
