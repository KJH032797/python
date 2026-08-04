def f01(x):
    print("f01 called")
    return x()

def f02():
    print("f02 called")
    return "exit"

f01(f02)
print()
print(f02())

# def f01(a=100,b = "apple", *c, **d):
#     print("f01 called")
#     print(a)
#     print(b)
#     print(c)
#     print(d)
#
# f01()