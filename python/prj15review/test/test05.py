N = int(input("enter the number : "))
table = []
value = 0

for i in range(N): #행(리스트의 개수)
    arr=[]
    for j in range(N): #열(리스트 안의 개수)
        arr.append(value)
    table.append(arr)

for x in table:
    print(x)
