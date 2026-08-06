# 컴프리헨션

# 0,1,2,3,4,...9

# result = [홀 or 짝]

# result = []
#
# for i in range(10):
#     if i % 2 == 0:
#         result.append("짝")
#     else :
#         result.append("홀")

result = ["짝" if i%2 == 0 else "홀" for i in range(10)]

print(result)