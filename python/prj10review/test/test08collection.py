# list, dictionary, tuple, set
from unittest import result

def func01() :
    a = [10, 30, 20, -10, -99]
    a.append(100)
    a.append(200)
    a.insert(2, 777)
    # remove, pop, del, sort, sorted, reversed

    a[0] = 123

    result = sorted(a)
    print(result)
    print(a)

def func02() : # dictionary
    personal = {"name" : "Kim", "age" : 25, "blood" : "O"}
    personal["age"] += 1
    print(personal)
    print(personal["name"])
    print(personal["age"])
    print(personal["blood"])
    # print(personal["MBTI"])
    print(personal.get("MBTI", "I"))
    print(list(personal.keys()))
    print(list(personal.values()))
    print(personal.items())
    print("age" in personal)

def func02_1() :
    x = {
        "p1" : {"name": "철수", "age": 20},
        "p2" : {"name": "영희", "age": 21},
        "p3" : {"name": "미영", "age": 30},
    }
    print(x)

def func03() : #set
    x = {10,20,30}
    y = {20,30,40}
    print(x|y)

def func04() : #tuple
    x = (10,20,30)
    x[0] = 123
    print(x[0])

func04()