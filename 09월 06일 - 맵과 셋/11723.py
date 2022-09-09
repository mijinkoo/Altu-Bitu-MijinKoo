# 알튜비튜
# 집합
import sys
input = sys.stdin.readline

m = int(input())
S = set()

def add(x):
    S.add(x)

def remove(x):
    if x in S:
        S.remove(x)

def check(x):
    if x in S:
        print(1)
    else:
        print(0)

def toggle(x):
    if x in S:
        S.remove(x)
    else:
        S.add(x)

for i in range(m):
    input_line = input().rstrip()

    if input_line == "all":
        S = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
            11, 12, 13, 14, 15, 16, 17, 18, 19, 20}
    elif input_line == "empty":
        S = set()
    else:
        str, x = input_line.split()
        x = int(x)
        if str == "add":
            add(x)
        elif str == "remove":
            remove(x)
        elif str == "check":
            check(x)
        elif str == "toggle":
            toggle(x)