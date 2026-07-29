def GetSum(x, y): # (x,y)매개변수 parameter
    result = x + y #문 안에 있는 변수 지정은 밖에서 인식 안 됨
    # print(result)
    return result #밖에서(GetSum)이 result로 인식되게함

temp = GetSum(10, 20)
print(temp)