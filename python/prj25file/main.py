# data.csv 파일 연결 (쓰기 모드)
import csv

def f01() -> None:
    with open("data.csv", "w", encoding="utf-8", newline='') as f:
        writer = csv.writer(f)
        # writer.writerow([111,222])
        # writer.writerow([333,444])
        # writer.writerow([555,666])
        writer.writerows([
            ["name", "age", "city"],
            ["홍길동", 20, "서울"],
            ["고길동", 40, "부산"]
        ])

# data.csv 파일 연결 (읽기 모드)
def f02() -> None:
    with open("data.csv", "r", encoding="utf-8") as f:
        # content = f.read()
        # print(content)
        data = csv.reader(f)
        for row in data:
            print(row)

# dict 기반 (write)
def f03() -> None:
    data = [
        {"name":"홍길동", "age":20, "city":"서울"},
        {"name":"고길동", "age":40, "city":"부산"}
    ]
    with open("data.csv", "w", encoding="utf-8", newline='') as f:
        fieldnames = ["name", "age", "city"]
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)


# dict 기반 (read)
def f04() -> None:
    with open("data.csv", "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            print(row)

