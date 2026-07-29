score_list = [100, 90, 100, 95, 80, 75]

# total = sum(score_list)
# avg = total / len(score_list)
#
# print(total)
# print(avg)

total = 0

for score in score_list:
    total += score
average = total / len(score_list)
print(total, average)