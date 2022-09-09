# 알튜비튜
import sys
input = sys.stdin.readline

n = int(input())
name_set = set()
for i in range(n):
    name, log = input().split()
    if log == "enter":
        name_set.add(name)
    elif log == "leave":
        name_set.remove(name)

name_list = list(name_set)
name_list.sort(reverse=True)
for s in name_list:
    print(s)