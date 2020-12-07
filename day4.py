import re

file1 = open('day4data', 'r')
lines = file1.readlines()

byr = False 
iyr = False
eyr = False
hgt = False
hcl = False
ecl = False
pid = False
count = 0

for line in lines:
    if line == "\n":
        if byr and iyr and eyr and hgt and hcl and ecl and pid:
            count += 1
        byr = False 
        iyr = False
        eyr = False
        hgt = False
        hcl = False
        ecl = False
        pid = False

    else: 
        entries = line.split(" ")
        for entry in entries:
            value = entry.split(":")[1]
            if "byr" in entry:
                year = int(value)
                if year >= 1920 and year <= 2002:
                    byr = True
            if "iyr" in entry:
                year = int(value)

                if year >= 2010 and year <= 2020:
                    iyr = True
            if "eyr" in entry:
                year = int(value)
                if year >= 2020 and year <= 2030:
                    eyr = True
            if "hgt" in entry:
                if "in" in value:
                    height = int(value.split("in")[0])
                    if height >= 59 and height <=76:
                        hgt = True
                if "cm" in value:
                    height = int(value.split("cm")[0])
                    if height >= 150 and height <= 193:
                        hgt = True
            if "hcl" in entry:
                if re.match("^#(\d|[a-f]){6}$", value) != None:
                    hcl = True
            if "ecl" in entry:
                print(entry)
                if "amb" in value or "blu" in value or "brn" in value or "gry" in value or "grn" in value or "hzl" in value or "oth" in value:
                    ecl = True
                print(ecl)
            if "pid" in entry:
                if re.match("^[0-9]{9}$", value) != None:
                    pid = True

if byr and iyr and eyr and hgt and hcl and ecl and pid:
        count += 1

print(count)
