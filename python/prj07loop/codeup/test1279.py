Num = input().split()
a = int(Num[0])
b = int(Num[1])
sum=0

for i in range(a, b+1):
    if i%2 == 0:
        sum-=i

    else :
        sum+=i

print(sum)


