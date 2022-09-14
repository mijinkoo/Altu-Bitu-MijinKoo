# 알튜비튜
# 자료구조 - 덱
# 시간초과
import sys
from collections import deque

input = sys.stdin.readline
n, k = map(int, input().split())

circle_dq = deque()
answer_dq = deque()

for i in range(1, n+1):
    circle_dq.append(i)

idx = k-1
while True:
    answer_dq.append(circle_dq[idx])
    circle_dq.remove(circle_dq[idx])
    
    if len(answer_dq) == n:
        break

    idx += k-1
    if idx > len(circle_dq)-1:
        idx = idx % len(circle_dq)

answer = ", ".join(map(str, list(answer_dq)))
print("<" + answer + ">")