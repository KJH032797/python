# row, col 입력 받아서 2차원 배열 생성 / 1부터 시작해서 1씩 증가

# 123 / 456 / 789
# 12345 / 678910 / 1112131415
# 12 / 34 / 56 / 78
# 1234 / 5678

arr = []
value = 1
row_number = int(input("row number: "))
col_number = int(input("column number: "))

for row in range(row_number):
    x=[]
    for col in range(col_number):
        x.append(value)
        value += 1
    arr.append(x)


for temp in arr:
    print(temp)