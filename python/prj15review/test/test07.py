#짝수행 1 / 홀수행 0

row_n=int(input("enter the row : "))
col_n=int(input("enter the col : "))
table=[]

for i in range(row_n) :
    arr=[]
    for j in range(col_n) :
        if i%2==0 :
            arr.append(1)
        else :
            arr.append(0)
    table.append(arr)

for x in table :
    print(x)