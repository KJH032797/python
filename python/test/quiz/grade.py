# 문제 맞춘 횟수
score = 0

# 등급
def grade(score):
    if score == 3:
        print("Your grade is A")
    elif score == 2:
        print("Your grade is B")
    elif score == 1:
        print("Your grade is C")
    else:
        print("Your grade is F")