
# import sys;sys.stdin=open('11650_input.txt')
# from collections import deque

# t = int(input())
# for x in range(1,t+1):
#     n,m = map(int,input().split())
#     ci = deque(map(int,input().split()))
#     q = deque()

#     for _ in range(n): # 첨에 피자 넣기
#         q.append(ci.popleft())

#     print(f'#{x} 남은피자', *ci)
#     print(f'#{x} 화덕', *q)
#     # 1. 남은 피자가 없고 2. 화덕에 있는 모든 피자가 1이하일 때 1인 피자를 찾고, 그 중 가장 마지막 피자가 남는 피자
#     while len(q) > 1:
#         q.append(q.popleft() // 2)

#         if q[-1] == 0: # 치즈 다 녹으면 화덕에서 꺼내기
#             q.pop()
#             if not ci: # 남은 피자 없으면 없는대로 돌리고
#                 pass
#             else:
#                 q.append(ci.popleft()) # 있으면 화덕에 피자 새로 넣기

#     print('결과', *q)

# -------------

import sys;sys.stdin=open('11650_input.txt')
from collections import deque

t = int(input())
for x in range(1,t+1):
    n,m = map(int,input().split())
    ci = deque(map(int,input().split()))
    ci = deque((i+1,ci[i]) for i in range(m))
    q = deque()

    for _ in range(n): # 첨에 피자 넣기
        q.append(ci.popleft())

    print(f'#{x} 남은피자', *ci)
    print(f'#{x} 화덕', *q)
    # 1. 남은 피자가 없고 2. 화덕에 있는 모든 피자가 1이하일 때 1인 피자를 찾고, 그 중 가장 마지막 피자가 남는 피자
    while len(q) > 1:
        idx, cheese = q.popleft()
        cheese //= 2

        if cheese > 0: # 치즈 다 안녹았으면
            q.append((idx, cheese)) 

        else:
            q.popleft()
            if ci:
                q.append(ci.popleft())
            else:
                pass


    print('결과', q[0][0])





#     a=[1,2,3]

#     print(all(a) >= 2)

# import sys;sys.stdin=open('11650_input.txt')
# from collections import deque

# t = int(input())
# for x in range(1,t+1):
#     n,m = map(int,input().split())
#     ci = deque(map(int,input().split()))
#     q = [0] * n
#     for i in range(n):
#         q[i] = ci[i]
#         ci.popleft()
#     print('남은피자',*ci)
#     print('화덕',*q)



    # q2 = [pizza // 2 for pizza in q]
    
    # q = q2


    
        




# 처음 리스트에 3개의 피자를 넣고 각 자리에 몇번째 피자인지 적고 계속 //2 돌린다.
# 치즈가 다 녹은 피자가 나오면 빼고 그 자리에 남은 피자를 넣고 몇번째 피자인지 교체
# 남은 피자가 다 떨어지면 화덕에 남은 피자 계속 //2
# 최후에 남은 피자가 몇번째 피자인지 출력ㅂㅃㅃㅃㅃㅃ