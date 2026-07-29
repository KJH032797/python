# 학생 3명의 성적 임의 작성 후 출력

std_grade = [{"name" : "kim", "score" : 100},
             {"name" : "lee", "score" : 80},
             {"name" : "oh", "score" : 90}]

for std_info in std_grade:
    print(f"{std_info['name']} 학생의 성적은 {std_info['score']}입니다.")