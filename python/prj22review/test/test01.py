x=[]

value=10

for i in range(3):
    temp = []
    for j in range(3):
        temp.append(value)
        value += 10
    x.append(temp)

print(x)
