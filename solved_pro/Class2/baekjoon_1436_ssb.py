'''
# 1(0)
0666 ~ 5666 (6개)
6660 ~ 6669 (10개)
7666 ~ 9666 (3개)
# 20(1)
10666 ~ 15666 (6개)
16660 ~ 16669 (10개)
17666 ~ 19666 (3개)
# 39(2)
20666~
.. 58(3), 77(4), 96(5)
# 115(6)
60666 ~ 65666 (6개)
66600 ~ 66699 (100개)
67666 ~ 69666 (3개)
앞: 0~9 + 뒤: 0~9 -1(겹) = 10+10-1 = 19
115~120(6개) > 121~220(100개) > 
'''
n = int(input())

cnt = 0
for i in range(1000000000):
    if '666' in str(i):
        cnt += 1
    if cnt==n:
        print(i)
        break