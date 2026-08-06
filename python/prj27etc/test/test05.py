#zip

names=["홍길동","임꺽정"]
scores=[100,200,300]
heights=[165,170,180]

data_list=zip(names,scores,heights)
for n,s,h in data_list:
    print(f"{n} / {s} / {h}")

print(data_list)