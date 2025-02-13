# T = int(input())

# for i in range(T):
#     N, M = map(int,input().split())
#     arr = list(map(int,input().split()))
    
# for j in range(N-1): # N-1번 반복
#     for j in range(N-1-i): # i = 이전에 정렬된 부분
#         if arr[j] > arr[j+1]: # 바로 옆에 있는 요소와 비교
#             arr[j], arr[j+1] = arr[j+1], arr[j] # 만약 앞이 더 크다면 둘이 자리를 바꿈


#     print(right3 - left3)
    
  
  
  
  
  
  
  
  
  
  
  
  
  
# N = 10

# # 1. 구간의 시작과 끝을 안다.
# start, end = 3, 7
# for i in range(start, end + 1):
#     lst[i] = '*'
    
# # 2. 구간의 시작과 길이를 안다.
# start, length = 3, 5
# for i in range(start, start + length):
#     lst[i] = '*'

# # 구간의 합을 구하기
# # 길이는 M, 시작은 알 수 없음
# N, M = 5, 3
# lst = [1] * N

# # 계산해야 되는 모든 구간의 시작 위치 계산
# # 시작 위치 = 0
# S = 0
# for i in range(S, S + M):
#     lst[i] = 0

# print(*lst)  
    

import sys; sys.stdin = open('4835.txt')

T = int(input())

for t in range(1, T + 1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))

    max_val = 0
    min_val = 1000000

# 모든 구간의 시작 인덱스를 생성
    for s in range(0, N - M + 1):
        # 구간 순회 시작은 s, 길이는 M
        SUM = 0
        for i in range(s, s + M):
            SUM += arr[i]
    
        if min_val > SUM:
            min_val = SUM
        
        if max_val < SUM:
            max_val = SUM
        
    print(f'#{t}', max_val - min_val)

