#Loads passports
with open('Day4_input.txt') as file:
    passports = file.read().split('\n\n')
#cleans up passports
passports=[p.replace("\n", " ") for p in passports]



#Part1
required_fields=["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
valid_eyes=["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
p1_valid=0
p2_valid=0
for p in passports:
    d = dict(x.split(':') for x in p.strip().split(' '))
    if all(req in d for req in required_fields):
        p1_valid+=1
        #Part2
        VALID=True
        for field in required_fields:
            if field=="byr":
                if int(d[field])<1920 or int(d[field])>2002:
                    VALID=False
            elif field=="iyr":
                if int(d[field])<2010 or int(d[field])>2020:
                    VALID=False
            elif field=="eyr":
                if int(d[field])<2020 or int(d[field])>2030:
                    VALID=False
            elif field=="hgt":
                if d[field][-2:]=="cm":
                    if int(d[field][:-2])<150 or int(d[field][:-2])>193:
                        VALID=False
                elif d[field][-2:]=="in":
                    if int(d[field][:-2])<59 or int(d[field][:-2])>76:
                        VALID=False
                else:
                    VALID=False
            elif field=="hcl":
                if d[field][0]!="#" or len(d[field])!=7:
                    VALID=False
            elif field=="ecl":
                if d[field] not in valid_eyes:
                    VALID=False
            elif field=="pid":
                if len(d[field])!=9:
                    VALID=False
        if VALID==True:
            p2_valid+=1
print(p1_valid)
print(p2_valid)