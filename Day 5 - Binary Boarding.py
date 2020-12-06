
seats=[x.strip() for x in open("Day5_input.txt","r")]

#Part1
def seat_id (row, column):
    return (int(row)*8)+int(column)
seat_ids=[]
for seat in seats:
    rows=[x for x in range(128)]
    cols=[x for x in range(8)]
    for letter in seat:
        if letter=="F":
            rows=rows[:len(rows)//2]
        elif letter=="B":
            rows=rows[len(rows)//2:]
        elif letter=="L":
            cols=cols[:len(cols)//2]
        elif letter=="R":
            cols=cols[len(cols)//2:]
    row=rows[0]
    col=cols[0]
    seat_ids.append(seat_id(row, col))

print(max(seat_ids))

#Part2
for id in range(max(seat_ids)+1):
    if id not in seat_ids and id+1 in seat_ids and id-1 in seat_ids:
        print(id)
