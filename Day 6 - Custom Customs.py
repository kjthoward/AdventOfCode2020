#Part 1
#Loads forms
with open('Day6_input.txt') as file:
    forms_file = file.read().split('\n\n')
#cleans up forms
forms=[f.replace("\n", "") for f in forms_file]
count=0
for form in forms:
    count+=len(set(form))
print(count)

#Part2
with open('Day6_input.txt') as f:
  groups = ''.join(f.readlines()).rstrip().split('\n\n')
  print(sum([len(set.intersection(*[set(line) for line in group.split('\n')])) for group in groups]))