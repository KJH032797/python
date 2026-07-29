# a=[]
# b=[]
# c=[]
# d=[]
# e=[]
#
# x =[a,b,c,d,e]
#
# # for i in range (1,6) :
# #     a.append(i)
# #     b.append(i)
# #     c.append(i)
# #     d.append(i)
# #     e.append(i)
# #
# # print(x)

x=[]
value=1

for i in range (3):
    arr=[]
    for j in range (1, 4):
        arr.append(value)
        value=value+1
    x.append(arr)

for temp in x:
    print(temp, end=" ")