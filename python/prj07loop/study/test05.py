# zip # list 두 개를 함께 묶음

people_name = ["철수", "영희", "꺽정"]
people_age = [20, 21, 33]

for name, age in zip(people_name, people_age):
    print(f"name : {name}, age : {age}")

