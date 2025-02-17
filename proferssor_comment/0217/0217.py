if arr[i] == 0:
    arr[i] = 1
elif arr[i] ==1:
    arr[i] = 0

# or 

arr[i] ^= 1 # : arr[i] = arr[i] ^ 1

# 이진탐색, 이분할
print(10 << 1)

# 홀짝 비교
print(10 & 1)
print(11 & 1)


# 2회차 과목평가 2번 문제

'''
0은 안전영역, 1은 r괴물, 2는 g괴물, 3은 b괴물, 4는 벽
광선은 상하좌우로 r괴물은 1칸, g괴물은 2칸, b괴물은 3칸
광선 도중에 벽을 만나거나 괴물이 있으면 중단 
'''

dr = [0,1,0,-1]
dc = [1,0,-1,0]

def gogo(arr,r,c): # 함수 생성
    l = arr[r][c]
    for dir in range(4):
        for i in range(l, l + 1):
            nr = r + dr[dir]*i
            nc = r + dr[dir]*i
            if nr < 0 or nr >= n or nc < 0 or nc >= n:
                break
            if l <= arr[nr][nc] <= 4:
                break
            arr[nr][nc] = 5

t = int(input())
for x in range(1,t+1):
    n = int(input())
    arr = [list(map(int,input())) for _ in range(10)]

    for r in range(10):
        for c in range(10):
            if arr[r][c] in (0,4,5):
                continue
            #(r,c 에 대해 네방향 탐색)
            gogo(arr,r,c)

ans = 0 # 카운팅
for r in range(10):
    for c in range(10):
        if arr[r][c] == 0:
            ans += 1
    print(ans)