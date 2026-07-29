import random
from quiz.quiz import Quiz_list
from quiz.quiz import Answer_dict
from quiz.grade import grade



def Re() :
    retry = input("네 or 아니오 :")
    if retry == "네":
        test()

    elif retry == "아니오":
        print("\n수고하셨습니다!")

    else:
        print("\n네, 아니오로만 대답해주세요.")
        Re()


# 조건문 / 반복문
def test() :
    score = 0
    # 5문제 중 랜덤으로 3문제 출제
    Quiz = random.sample(Quiz_list, 3)
    print("\n시험을 시작합니다. 시험을 그만두시려면 \"시험종료\"를 입력해주세요.")

    for i, question in enumerate(Quiz, 1):
        print(f"\nQ{i} : {question}")
        correct = Answer_dict[question]
        user_answer = input("A : ")

        if user_answer == "시험종료" : #유저입력 종료처리
            print("수고하셨습니다!")
            return


        if user_answer.lower().strip() == correct.lower().strip(): #대소문자 구분X
                print("정답입니다!\n")
                score += 1

        else:
            print("오답입니다.")
            print(f"{correct}\n") # 오답시 정답 확인

    print(f"정답 횟수는 {score}입니다.") # 맞춘 문제 수
    grade(score)
    print("재시험을 보시겠습니까?") #재시도
    Re()