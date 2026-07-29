# 컴프리헨션

x = [10,20,30,40,50]
y = []

# 1
for elem in x:
    if elem <= 30 :
        y.append(elem + 1)
# 2
# y = [elem +1 for elem in x if elem <= 30]

print(y)