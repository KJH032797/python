table = [
    [10,20,30],
    [40,50,None],
    [70,80,90],
    [100,110,120],
    [130,140,150],
    [None,170,180],
    [190,200,210],
    [220,230,None]
]

# for i in table :
#     for j in i :
#         if j is None:
#             table.remove(i)
#
# print(table)

x = len(table)
y=0
z = len(table[y])

for i in range(x) :
    for j in range(z) :
        if table[y][j] is None:
            table.remove(table[y])
            y-=1
    y+=1

print(table)

