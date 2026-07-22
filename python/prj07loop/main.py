Num = input().split()
a = int(Num[0])
b = int(Num[1])

sum=0

# a부터 b까지 계산, 홀수/짝수 구분, 조건에 따라 계산
while a <= b:
    sum = sum + a
    if a % 2 == 0:
        print(f"{a} + {sum} = {a+sum}")
        a += 1
    elif a % 2 != 0:
        sum = sum - a
        print(f"{-a} - {sum} = {-a-sum}")
    a = a+1




# if a%2==0:
#     if b%2==0 :
#         print(a+b)
#     else:
#         print(a-b)
# else :
#      if b%2==0:
#             print(-a+b)
#      else:
#          print(-a - b)
