names=["김","이","박"]
subjects=["국","영","수"]

table = []

for i in range(len(names)) :
    arr=[]
    for j in range(len(subjects)) :
        arr.append(0)
    table.append(arr)

table[0][0] = 40
table[0][1] = 90
table[0][2] = 80
table[1][0] = 10
table[1][1] = 20
table[1][2] = 30
table[2][0] = 70
table[2][1] = 60
table[2][2] = 50

# avg_list = []
# total_list=[]
# student_avg = []
# sub_score = [] 나


#과목별 평균
# for i in range(3) : 나
#     avg=0
#     for j in range(3) :
#         avg += table[j][i] / len(names)
#         sub_score.append(table[j][i])
#     avg_list.append(avg)

# for i in range(3) :
#     print(f"{subjects[i]} : {avg_list[i]}")
"============================================"
total = [0,0,0]
avg = [0,0,0]
for j in range(len(names)) : #강사님
    for i in range(len(names)) :
        total[j] += table[i][j]
    avg[j] = total[j] / len(names)

print("과목별 평균")
for i in range(3) :
    print(f"{subjects[i]} : {avg[i]}")



#학생별 총점&평균

#나
# for i in range(3) :
#     total = 0
#     for score in table[i]:
#         total += score
#     total_list.append(total)
#
# for i in range(3) :
#     total_avg = total_list[i] / len(subjects)
#     student_avg.append(total_avg)
#
# for i in range(3) :
#     print(f"{names[i]} : 총점 {total_list[i]}, 평균 {student_avg[i]}")


#강사님
student_total_list = []
student_mean_list = []

for i in range(len(names)) :
    total = 0
    for j in range(len(subjects)) :
        total += table[i][j]
    student_total_list.append(total)

print("\n학생별 총점과 평균")
for i in range(len(names)) :
    print(f"{names[i]} 학생의 총점은 {student_total_list[i]}이고, "
          f"평균은 {student_total_list[i] / len(subjects)}입니다.")

"============================================="

#과목별 최고점수와 해당 학생명

# 나
# sub_score_list = [sub_score[0:3],sub_score[3:6],sub_score[6:10]]
# top=0
# for i in range(3) :
#     for j in range(3) :
#         if top < sub_score_list[i][j]:
#             top = sub_score_list[i][j]
#     print(f"{subjects[i]} 최고점수 : {top}, {names[i]}")


# 강사님
top_list = []
top_idx_list = []

for i in range(len(subjects)) :
    top = -1
    top_idx = -1
    for j in range(len(names)) :
        if top < table[j][i]:
            top = table[j][i]
            top_idx = j
    top_list.append(top)
    top_idx_list.append(top_idx)

print("\n과목별 최고점수와 해당 학생명")
for i in range(len(names)) :
    top_scorer = top_idx_list[i]
    print(f"{subjects[i]} 성적 우수자 : {names[top_scorer]}, 점수 : {top_list[i]}")

"================================================"

#총점 최고득점자, 최저득점자 이름

# 나
# top_score = 0
# for i in range(3) :
#     if top_score < total_list[i]:
#         top_score = total_list[i]
#         idx = i
# print(f"총점 최고득점자 : {names[idx]}")

# bottom_score = 100
# for j in range(3) :
#     if total_list[j] < bottom_score :
#         bottom_score = total_list[j]
#         idx = j
# print(f"총점 최저득점자 : {names[idx]}")


# 강사님
# std_total_list = []
# for i in range(len(names)) :
#     std_score = table[i]
#     std_total = std_score[0] + std_score[1] + std_score[2]
#     std_total_list.append(std_total)
# print(std_total_list)
#
# top = -1
# top_idx = -1
# bottom = 301
# bottom_idx = -1
# for i in range(len(names)) :
#     if top < std_total_list[i]:
#         top = std_total_list[i]
#         top_idx = i
#     if bottom > std_total_list[i]:
#         bottom = std_total_list[i]
#         bottom_idx = i
# print("\n총점 최고득점자&최저득점자")
# print(f"총점 최고득점자 : {names[top_idx]}, 최고점 {top}\n"
#       f"총점 최저득점자 : {names[bottom_idx]}, 최저점 {bottom}")


# 강사님 총점 리스트 활용해 다시 해본것
# sum_top = -1
# top_index = -1
# sum_bot = 301
# bot_index = -1
# for i in range(len(names)) :
#         if sum_top < student_total_list[i]:
#             sum_top = student_total_list[i]
#             top_index = i
#         if sum_bot > student_total_list[i]:
#             sum_bot = student_total_list[i]
#             bot_index = i
#
# print(f"총점 최고득점자 : {names[top_index]}, 최고점 {sum_top}\n"
#       f"총점 최저득점자 : {names[bot_index]}, 최저점 {sum_bot}")

"================================================"

#평균 60점 미만 출력
# for i in range(3) : 나
#     if student_avg[i] < 60 :
#         print(f"{names[i]} : 평균 {student_avg[i]}")

"================================================"

#과락(40점)자 출력
# if sub_score_list[i][j] <= 40
#     print(f"{names[i]}")
# print(sub_score_list)




