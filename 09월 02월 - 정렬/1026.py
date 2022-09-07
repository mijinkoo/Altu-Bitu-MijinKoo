# 알튜비튜
# 보물

# 입력받기
import sys
input = sys.stdin.readline

# 입력 받기
n = int(input())
list_a = list(map(int, input().split()))
list_b = list(map(int, input().split()))

def main(a, b):
    a.sort()
    b.sort(reverse=True)

    res = 0
    for i in range(len(a)):
        res += a[i]*b[i]

    return res

print(main(list_a, list_b))