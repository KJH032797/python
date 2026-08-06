# 파일 읽기
import csv

with open("sales.csv", "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    data = list(reader)

# 전체 매출
total = 0
for row in data:
    total += int(row["단가"])*int(row["수량"])
# print(total)

# 메뉴별 판매량
qty_by_menu = {}
for row in data:
    # print(row["메뉴"], row["수량"])
    m = row["메뉴"]
    n = row["수량"]
    p = row["단가"]
    qty_by_menu[m] = qty_by_menu.get(m,0) + int(n) * int(p)
print(qty_by_menu)

# 베스트 메뉴
# best_menu = ""
# max_value = -1
# for k,v in qty_by_menu.items():
#     if max_value < v :
#         max_value = v
#         best_menu = k
#
# best_menu = max(qty_by_menu, key=qty_by_menu.get) # callback func
# print(best_menu)

# 카테고리별 매출

# 베스트 카테고리

# 월별 매출
sales_by_month = {}
for row in data:
    d = row["날짜"][:7]
    sales = int(row["수량"]) + int(row["단가"])
    sales_by_month[d] = sales_by_month.get(d,0) + sales

# print(sales_by_month)

# 리포트 파일 저장
# with open("report.txt", "w", encoding="utf-8") as f:
#     f.write("===== 카페.py 매출 리포트 (2025 1분기) =====\n\n")
#     f.write(f"[전체 매출] {total:,}won\n\n")
#     f.write(f"[메뉴별 총 판매금액]\n")
#     for k,v in qty_by_menu.items():
#         f.write(f"{k}: {v:,}won\n")