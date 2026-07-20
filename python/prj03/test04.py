# list

x=["apple", "strawberry", "banana", 3.27, True, "egg"]
print(x)
# print(x[0])
# x[0]="egg"
# print(x[0:6:2]) # begin:end:step
# x[1:3]=["grape", 3,4,5,45] #수정, 삭제[]
# print(x)
#
# x.append(777) #맨 뒤에 추가
# x.insert(1,"임요한") #가운데 추가 가능
# print(x)
# x.remove("임요한")
# print(x)
# x.clear() # 전체삭제

y=["pedri", "rodri", "messi", "messi", "mbappe"]
# x.append(y) # 전체 추가
# print(x)
x.extend(y) # 개별 추가 / ==x+y
print(x)
# x.pop

# name = x.index("messi") #()가 몇 번째에 있는지
# print(name)

# cnt=x.count("messi") # ()가 몇 개 있는지
# print(cnt)

# x.sort()
# print(x)
x.reverse() # 순서 뒤바꿈
print(x)

x2=x
print(x2)


x[0]="kane"
print(x)
print(x2)