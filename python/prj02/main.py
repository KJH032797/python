#unpacking, packing

a=["집에","가고","싶다"]
b=("집이","너무","멀다")

s,w,v=a
x,*y,z=b
print(w,v,s,x,y,z)

students=[('김철수',85),('이영희',92),('박민수',78)]

# 1) 모든 학생 이름과 점수 세트를 출력

# print(students[0])
# print(students[1])
# print(students[2])

# 2) 이름만 출력

# print(students[0][0])
# print(students[1][0])
# print(students[2][0])

# 3) 점수만 출력

# print(students[0][1])
# print(students[1][1])
# print(students[2][1])

print(type(students[0][1]))
print(float(students[0][1]))