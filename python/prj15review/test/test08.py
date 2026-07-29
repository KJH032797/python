
names=["김","이","박"]
subjects=["국","영","수"]

student = 3
test_num = 3
table = []

for i in range(student) :
    arr=[]
    for j in range(test_num) :
        arr.append(0)
    table.append(arr)

# table[0][0] = 40
# table[0][1] = 90
# table[0][2] = 80
# table[1][0] = 10
# table[1][1] = 20
# table[1][2] = 30
# table[2][0] = 70
# table[2][1] = 60
# table[2][2] = 50

total_list=[]

for i in range(3) :
    total = 0
    for score in table[i]:
        total += score
    total_list.append(total)

print(f"total_list : {total_list}")

idx=-1
top = 0

for i in range(3) : # greedy
    if total_list[i] > top :
        top = total_list[i]
        idx = i

print(f"top : {top}, idx : {idx}, names : {names[idx]}")


