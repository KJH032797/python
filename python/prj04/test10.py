# Python 점수와 Java 점수를 입력받으세요.
# 다음 조건을 모두 만족해야 통과입니다.
# - Python 60점 이상
# - Java 60점 이상
# - 두 과목 평균 70점 이상
# 결과를 `True`, `False`로 출력하세요.

Python_score=int(input("Python 점수 : "))
Java_score=int(input("Java 점수 : "))

sum=Python_score+Java_score
avg=sum/2

a=Python_score>=60
b=Java_score>=60
c=avg>=70
terms=a and b and c

print(f"통과 여부 : {terms}")