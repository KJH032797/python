a=list(range(3))
b=list(range(3))
c=list(range(3))

x=[a,b,c]

value = 10
i = 0

for j in range(3):
    for i in range(3):
        x[j][i] = value
        value += 10

# x[0] = [10,20,30]
# x[1] = [40,50,60]
# x[2] = [70,80,90]



print(x)

# 10,20,30/ 40,50,60/ 70,80,90