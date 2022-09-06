# 알튜비튜
# 좌표 정렬하기2
import sys
input = sys.stdin.readline

# 입력 받기
n = int(input())
input_list = []
for i in range(n):
    a, b = map(int, input().split())
    input_list.append((a, b))

# 정렬하고 출력하기
def sortAndPrint(list, n):
    list.sort(key=lambda x: (x[1], x[0]))

    for x in list:
        print(x[0], end=' ')
        print(x[1])

sortAndPrint(input_list, n)