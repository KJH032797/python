import random

from model.kkobugi import Kkobugi
from model.pielee import Pielee
from model.pikachu import Pikachu
from model.poketmon import Poketmon

def battle(attacker, defender):
    print(f"\"{attacker.name}\"가 \"{defender.name}\"를 공격 !")
    defender.hp -= (attacker.atk - defender.defe)
    print(f"attacker : {attacker}")
    print(f"defender : {defender}")

#포켓몬 객체 생성
p1 = Pikachu()
p2 = Pielee()
p3 = Kkobugi()

#포켓몬 목록 출력
print("----- Pokemon list-----")
print(1, p1)
print(2, p2)
print(3, p3)
print()

# 포켓몬 선택

num = int(input("원하는 포켓몬 번호를 입력하세요 : "))
match num :
    case 1 : user = Pikachu()
    case 2 : user = Pielee()
    case 3 : user = Kkobugi()


num = random.randint(1, 3)
match num :
    case 1 : com = Pikachu()
    case 2 : com = Pielee()
    case 3 : com = Kkobugi()


while True :
    # 유저 공격
    battle(user, com)
    if com.hp <= 0:
        print("user WIN !")
        break

    # 컴퓨터 공격
    battle(com, user)
    if user.hp <= 0:
        print("user LOSE !")
        break




