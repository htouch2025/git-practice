import time
import os

def timer(sec):
    while sec >= 0:
        print(f'倒计时：{sec:02d}秒', end = '\r')
        sec -= 1
        time.sleep(1)
    os.system('say "计时结束"')

timer(5)
print('')
 