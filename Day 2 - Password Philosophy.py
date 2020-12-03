#Part1
valid=0
for line in open("Day2_input.txt","r"):
    line=line.strip()
    numbers, letter, password = line.split()
    min,max=numbers.split("-")
    letter=letter.strip(":")
    occurance=password.count(letter)
    if occurance>=int(min) and occurance<=int(max):
        # print(min, max, letter, password)
        # import pdb; pdb.set_trace()
        valid+=1
print(valid)

#Part2
valid=0
for line in open("Day2_input.txt","r"):
    line=line.strip()
    numbers, letter, password = line.split()
    letter=letter.strip(":")
    i,j=numbers.split("-")
    i,j=int(i),int(j)
    #decrease by 1 so index 0'd
    i-=1
    j-=1
    # import pdb; pdb.set_trace()
    if (password[i]==letter and password[j]!=letter) or (password[i]!=letter and password[j]==letter):
        valid+=1
print(valid)
