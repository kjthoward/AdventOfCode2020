numbers=[x.strip() for x in open("Day1_input.txt","r").readlines()]

# Part 1
for i in range(len(numbers)):
    for num in numbers:
        if numbers[i]!=num:
            total=int(numbers[i])+int(num)
            if total==2020:
                print(int(numbers[i])*int(num))
                


#Part 2
for i in range(len(numbers)):
    for j in range(len(numbers)):
        for num in numbers:
            if numbers[i]!=num and numbers[j]!=num:
                total=int(numbers[i])+int(num)+int(numbers[j])
                if total==2020:
                    print(int(numbers[i])*int(num)*int(numbers[j]))
                    