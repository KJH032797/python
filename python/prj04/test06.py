# 시험 점수를 입력받아 점수가 60점 이상인지 출력하세요.
# 점수: 70
# True

test_score=int(input("시험 점수 : "))
terms = test_score>=60
print(f"{test_score}>=60", terms)