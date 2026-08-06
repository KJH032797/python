# thread
import threading
from time import time,sleep

for i in range(10):
    print(time())
    sleep(0.1)

def f01():
    for i in range(10):
        print("hello")
        sleep(0.1)

def f02():
    for i in range(10):
        print("world")
        sleep(0.1)

t1=threading.Thread(target=f01)
t2=threading.Thread(target=f02)

t1.start()
t2.start()

print("end~~~")