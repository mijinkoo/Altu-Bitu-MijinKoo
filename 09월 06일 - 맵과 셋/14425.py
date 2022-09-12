# 알튜비튜
import sys
input = sys.stdin.readline

# 입력받기
n, m = map(int, input().split())
S = set()
input_list = [0 for _ in range(m)]
for _ in range(n):
    S.add(input().rstrip())
for i in range(m):
    input_list[i] = input().rstrip()

answer = 0
for x in input_list:
    if x in S:
        answer += 1

print(answer)