# 알튜비튜
import sys
input = sys.stdin.readline

input_list = list(map(int, input().split()))
sum = int(input())
output_list = []
input_list.sort()

for i in range(len(input_list)-1):
    for j in range(i+1, len(input_list)):
        if input_list[i]+input_list[j]==sum:
            if input_list[i] >= input_list[j]:
                output_list.append((input_list[j], input_list[i]))
            else:
                output_list.append((input_list[i], input_list[j]))

output_list.sort()
output_list = list(dict.fromkeys(output_list)) # 리스트에서 기존 순서 유지하고 중복 제거하기

for t in output_list:
    print(t[0], end=' ')
    print(t[1])
print(len(output_list))