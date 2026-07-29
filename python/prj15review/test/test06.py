x=[]
n=0
value=1

#나
# for i in range(3) :
#     arr=[]
#     for j in range(3) :
#         arr.append(n)
#     x.append(arr)
#
# for i in x:
#     x[n][n] = value
#     n += 1
#     print(i)

#강사님
for i in range(3) :
    arr=[]
    for j in range(3) :
        if i == j :
            arr.append(value)
        else :
            arr.append(n)
    x.append(arr)

for i in x:
    print(i)

