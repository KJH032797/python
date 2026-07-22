#1~10 중에서 3의 배수의 합

n=1
result=0
while n<=10:
    if n % 3 == 0:
        result= result + n
    n=n+1

print(result)
