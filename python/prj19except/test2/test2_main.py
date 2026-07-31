def f01():
    print("f01 called")
    f02()
    print("f02 finished")

def f02():
    print("f02 called")
    result = 1 / 0
    print(result)
    f03()
    print("f02 finished")

def f03():
    print("f03 called")
    print("f03 finished")

f01()
if f01() is Exception:
    print("Error")
else :
    print("program is successful")