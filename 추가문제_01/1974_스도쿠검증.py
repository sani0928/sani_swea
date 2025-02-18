import sys;sys.stdin=open('1974_sample.txt')


    
def Search(puzzle):
    
    # 행우선 탐색
    for r in range(9):
        lst = [i for i in range(1,10)]
        for c in range(9):
            if puzzle[r][c] in lst:
                # lst는 오름차순, 인덱스 값은 실제 정수 값의 -1
                # 0으로 처리해서 제거
                lst[puzzle[r][c]-1] = 0 
            else:
                return 0 # 겹치는 부분이 있으면 0 반환

    # 열우선 탐색
    for c in range(9):
        lst = [i for i in range(1,10)]
        for r in range(9):
            if puzzle[r][c] in lst:
                lst[puzzle[r][c]-1] = 0
            else:
                return 0

    # 3x3 정사각 탐색
    for i in range(0,9,3): # 한 사각형 끝나면 옆에 사각형으로
        lst = [i for i in range(1,10)] # [1,2,3,4,5,6,7,8,9]
        for r in range(3):
            for c in range(3):            
                if puzzle[r+i][c+i] in lst:
                    lst[puzzle[r+i][c+i]-1] = 0
                else:
                    return 0
    return 1 # 끝까지 else에 안 걸리면 1 반환

t = int(input())
for x in range(1,t+1):
    arr = []
    for _ in range(9):
        arr.append(list(map(int,input().split())))
    
    
    print(f'#{x}',Search(arr))