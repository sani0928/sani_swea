import sys;sys.stdin=open('2817_input.txt')
import itertools

# from collections import deque

# t=int(input())
# for x in range(1,t+1):
#     n,k = map(int,input().split())
#     q = list(map(int,input().split()))
#     count = 0
#     # 1개 합이 k일 때
#     for l in range(n):
#         if q[l] == k:
#             count += 1
#     # 2개 합이 k일 때
#     for i in range(n):
#         for j in range(i+1,n):
#             if q[i] + q[j] == k:
#                 count += 1


#     print(f'#{x}',count)


t=int(input())
for x in range(1,t+1):
    n,k = map(int,input().split())
    q = list(map(int,input().split()))
    count = 0
    for i in range(1, n+1):
        for j in itertools.combinations(q,i):
            if sum(j) == k:
                count += 1
    print(f'#{x}',count)