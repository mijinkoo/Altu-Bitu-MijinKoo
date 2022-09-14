# 알튜비튜
# 자료구조
import sys
from collections import deque
input = sys.stdin.readline
input_dq = deque()
count_dq = deque()
ans = []

while True:
    # 입력 받기
    input_str = input().rstrip()
    if list(input_str)[0] == '-':
        break
    
    # 문자열에서 안정적인 괄호쌍들 제거하기
    st = [] # 불안정한 괄호쌍만 남기기
    for i in input_str:
        if i == '{':
            st.append('{')
        elif i == '}':
            if len(st) > 0 and st[-1] == '{':
                st.pop()
            else:
                st.append('}')

    # 필요한 최소 연산 횟수 구하기
    if len(st) == 0:
        ans.append(0)
    else:
        cnt = 0
        i = 0
        while i <= len(st)-2:
            if st[i]=='{':
                if st[i+1]=='{':
                    cnt += 1
                    i += 2
            elif st[i]=='}':
                if st[i+1] == '}':
                    cnt += 1
                    i += 2
                elif st[i+1] == '{':
                    cnt += 2
                    i += 2
        ans.append(cnt)

# 출력하기
if len(ans) > 0:
    for i in range(len(ans)):
        print(i+1, end='. ')
        print(ans[i])