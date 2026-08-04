# 예외 처리

try: # 예외 발생 시
    pass # 실행 시도
except 예외타입 | 예외타입 as x: # try블럭 내 예외 타입 일치시 잡아서 처리
    pass
except 예외타입 as y: # 예외 타입 여러개 설정 가능, 위에서부터 처리(범위 설정은 좁은 순부터 넓혀가기)
    pass
else: # 예외 없을 시 실행
    pass
finally: # 예외 있든 없든, return이 있어도 무조건 실행
    pass