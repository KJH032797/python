n=int(input())
i = 0
sum = 0
while True :
    sum += i
    if sum >= n :
        print(i)
        break

    else :
        i += 1
#         if i == 1:
#             print(f"{i}", end="")
#         else :
#             print(f"+{i}", end="")
#
# print(f"={sum}", end="")