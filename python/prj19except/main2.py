from dog import Dog

age = int(input("your age : "))
if age < 0 :
    print("impossible age is under 0")
    raise Dog("나이가 어떻게 음수")
print(age)