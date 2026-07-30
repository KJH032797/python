#연산자 테스트
from builtins import print
from operator import and_

#산술 : +, - *, **, /, //, %
# print(10+3)
# print(10/3)
# print(10//3)
# print(10%3)
# print(10*3)

#비교 <, > , <=, >=, ==, !=
# print(10<3)
# print(10>3)
# print(10>=3)
# print(10<=3)
# print(10==3)
# print(10!=3)

#논리 : not, and, or 순으로 적용, () 먼저 적용됨
print(not True and False)
print(not False and True)
print(not True and False or False)
print(not True and False or True)
print(not True or False and False)
print(not True or True and False)
# print(True or False)

#리스트
# correct=(1,2,5,4,3,2,4,1,2,3)
# A_answer=int(input("your answer:"))
# B_answer=int(input("your answer:"))
# C_answer=int(input("your answer:"))
# # if A_answer==correct:

# correct_score_list=[]
# correct_score_list.append(int(input("student score: ")))
# correct_score_list.append(int(input("student score: ")))
# correct_score_list.append(int(input("student score: ")))
# print(correct_score_list)+5

# print(correct_score_list[0])
# print(type(correct_score_list[0]))

# Q3. list ["김", "이," 박", "이", "최"]에서
# "이"가 몇 번 나오는지 출력하고 "박"의 위치(인덱스)출력.

# last_name_list=["김", "이", "박", "이", "최"]
# cnt=last_name_list.count("이")
# fnd=last_name_list.index("박")
# print(cnt)
# print(fnd)
#
# # Q4. list [1,2,3,4,5,6,7,8,9,10]에서 슬라이싱만 사용해 아래를 각각 출력하세요.
# list=[1,2,3,4,5,6,7,8,9,10]
# #1. 앞 3개 > [1,2,3]
# print(list[0:3])
# #2. 뒤 3개 > [8,9,10]
# print(list[7:10])
# #3. 짝수 인덱스 값만 > [1,3,5,7,9]
# print((list[1:10:2])
#
# # e_num=list[1:10:2]
# # print(e_num)
# # e_index=list.index(2)
# # print((e_index))
# #4. 전체 역순 > [10,9,8,...,1]
# list.reverse()
# print(list)