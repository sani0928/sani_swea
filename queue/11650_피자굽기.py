import sys;sys.stdin=open('11650_input.txt')
from collections import deque

t = int(input())
for x in range(1,t+1):
    n,m = map(int,input().split())
    ci = deque(map(int,input().split()))
    n2 = n
    q = []
    nametag = []

    for _ in range(n):
        q.append(ci.popleft())

    print(f'#{x} 남은피자', *ci)
    print(f'#{x} 화덕', *q)
    i = 0
    while len(q) < n:
        
        for i in range(i, n2):
            q[i]//2
            if q[i] <= 0:
                q[i] = 0
                nametag.append(i)
                q.append(ci.popleft())
        
        n2 += 1
        i += 1
            



#     print('결과', *q)

# import sys;sys.stdin=open('11650_input.txt')
# from collections import deque

# t = int(input())
# for x in range(1,t+1):
#     n,m = map(int,input().split())
#     ci = deque(map(int,input().split()))
#     ci = deque((i+1,ci[i]) for i in range(m))
#     q = deque()

#     for _ in range(n):
#         q.append(ci.popleft())
    
#     print(f'#{x} 남은피자', *ci)
#     print(f'#{x} 화덕', *q)
#     # 1. 남은 피자가 없고 2. 화덕에 있는 모든 피자가 1이하일 때 1인 피자를 찾고, 그 중 가장 마지막 피자가 남는 피자
#     while ci != deque() and all(q) >= 1 and and and:
#         idx,cheese = q.popleft()
#         cheese // 2
        
#         if q[-1] == 0: # 치즈 다 녹으면 화덕에서 꺼내기
#             q.pop()
#             if not ci: # 남은 피자 없으면 없는대로 돌리고
#                 pass
#             else:
#                 q.append(ci.popleft()) # 있으면 화덕에 피자 새로 넣기

#     print('결과', *q)


#     a=[1,2,3]

#     print(all(a) >= 2)