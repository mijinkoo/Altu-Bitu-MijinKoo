# 알튜비튜
# 해시를 사용한 집합과 딕셔너리
import sys
input = sys.stdin.readline

n, c = map(int, input().split())
input_list = list(map(int, input().split()))
input_setList = list(dict.fromkeys(input_list)) # 기존 순서 보존하면서 중복 제거하기
input_dict = {} # 데이터를 빈도수랑 같이 저장하기

for x in input_setList:
    cnt = 0
    for y in input_list:
        if y == x:
            cnt += 1
    input_dict[x] = cnt

# 딕셔너리에서 value 값을 기준으로 내림차순 정렬
sorted_dict = dict(sorted(input_dict.items(), key=lambda x: x[1], reverse=True))

for k, v in sorted_dict.items():
    for i in range(v):
        print(k, end=' ')