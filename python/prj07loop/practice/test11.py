# 1 ~ 10 중에서, 홀수만 출력

# x = [1,2,3,4,5,6,7,8,9,10]
x = range(1,11)
print(x)
print(type(x))
for i in x:
    # if i%2==0:
    #     continue
    print(i, end=' ')