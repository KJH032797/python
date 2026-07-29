def judgeUpDown(answer, num):
    if num < answer:
        print("up")
    elif num > answer:
        print("down")
    else:
        print("right")
        return True