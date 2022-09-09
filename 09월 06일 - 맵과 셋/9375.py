# 알튜비튜
import sys
input = sys.stdin.readline

n = int(input())
for i in range(n):
    
    m = int(input())
    wear_dict = dict()

    for j in range(m):
        v, k = input().split()
        if k in wear_dict.keys():
            wear_dict[k] += 1
        else:
            wear_dict[k] = 1

    cnt_list = list(wear_dict.values())
    if len(cnt_list) == 1:
        print(cnt_list[0])
    else:
        ans = 1
        for c in cnt_list:
            ans *= (c+1)
        print(ans-1)