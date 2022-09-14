# 알튜비튜
# 자료구조
import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
input_list = list(map(int, input().split()))
input_list.reverse() # 순서 바꾸기

result_dq = deque()
for i in range(n):
    if input_list[i] == 1:
        result_dq.appendleft(i+1)
    elif input_list[i] == 2:
        result_dq.insert(1, i+1)
    elif input_list[i] == 3:
        result_dq.append(i+1)

print(*result_dq)