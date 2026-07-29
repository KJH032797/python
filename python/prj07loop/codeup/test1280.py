Num = input().split()
a = int(Num[0])
b = int(Num[1])

sum=0

for i in range(a, b+1):
    if i%2 == 0:
        print(f"-{i}", end="")
        sum-=i

    else :
        print(f"+{i}", end="")
        sum+=i

print(f"={sum}", end="")

