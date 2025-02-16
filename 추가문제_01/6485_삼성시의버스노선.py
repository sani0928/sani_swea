import sys;sys.stdin=open('6485_input.txt')

t = int(input())
for x in range(1,t+1):
    n = int(input()) # n>2이 되면 인풋은 어떻게 받지?

    counts = [0] * 5000 # 전체 버스 정류장과 겹치는 노선 카운팅용

    for _ in range(n):
        Ai,Bi = map(int,input().split())
        for i in range(Ai,Bi+1): # 겹치는 버스 노선을 카운팅
            counts[i-1] += 1
        # 1 1 1 0 0 0 0 0 0 ... 0
        # 1 2 2 1 1 0 0 0 0 ... 0
    
    p = int(input())
    result = []

    for _ in range(p):
        cj = int(input())
        result.append(counts[cj-1]) # cj-1의 값 = counts 인덱스 값 안에 있는 겹치는 버스 노선
    print(f'#{x}', *result)
        
# t = int(input())
# for x in range(1,t+1):
#     n = int(input()) # n>2이 되면 인풋은 어떻게 받지?
#     AiBi_lst = []
#     for _ in range(n):
#         AiBi_lst.append(list(map(int,input().split())))
#     print(AiBi_lst)

        
#     p = int(input())
#     counts = [0] * p # 카운팅용

#     for i in range(p):
#         cj = int(input())
#         for j in range(n):
            
#             if AiBi_lst[j][j] <= cj <= AiBi_lst[j][j+1]: #ai과 bi 사이에 있으면 카운팅
#                 counts[cj-1] += 1
    
#             if AiBi_lst[j+1][j] <= cj <= AiBi_lst[j+1][j]: #aj과 bj 사이에 있으면 카운팅
#                 counts[cj-1] += 1            

    
#     print(f'#{x}', *counts)
        