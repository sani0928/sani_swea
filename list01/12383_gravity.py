import sys;sys.stdin=open('12383_input.txt')

t = int(input())
for x in range(1, t+1):
    n = int(input())
    lst = list(map(int,input().split()))
    arr = [[0]*(max(lst)) for _ in range(n)] # 미리 90도 돌린 배열 생성

    for i in range(n): # 블록 생성 (0은 빈 공간, 1은 블록)
        for j in range(lst[i]):
            arr[i][j] = 1

    cnt = 0 # 낙차거리 카운팅
    total_cnt = []
    # 아래에서 위로 열우선 역순회
    for c in range(max(lst)):
        for r in range(n-1,-1,-1):
            if arr[r][c] == 1: # 블록 발견시
                i = r
                while i+1 < n: # 바닥까지 떨어짐              
                    if arr[i+1][c] == 0: # 다음 칸 아래가 빈 공간이면
                        arr[i][c] = 0 
                        arr[i+1][c] = 1 # 떨어짐
                    else: # 다음 칸 아래에 블록이 있으면
                        break # 정지
                    i+=1 # 다음 칸 이동
                    cnt += 1 # 낙하 한칸씩 카운팅
                    
                total_cnt.append(cnt) # 총 낙차거리 저장
                cnt = 0 # 카운팅 초기화

    print(f'#{x}', max(total_cnt))
