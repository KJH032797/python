# 초를 입력받아 몇 시간, 몇 분, 몇 초인지 계산하세요.
# 예를 들어 3725초는 1시간 2분 5초입니다.
# 출력 예시:
# 초를 입력하세요: 3725
# 1 시간 2 분 5 초

current_sec=int(input("초를 입력하세요 : "))
hour=int(((current_sec/60)/60))
min=int(((current_sec%60)/60)+((((current_sec/60)//60))*60))
sec=int(current_sec%60)
print(f"{hour}시간 {min}분 {sec}초")