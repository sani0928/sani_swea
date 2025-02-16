'''
🚀 델타 탐색 기초 연습 문제: “숫자 더하기 게임” 😊
📝 문제 설명:
N x N 크기의 2차원 배열이 주어집니다.

각 칸에는 **숫자(1~9)**가 적혀 있습니다.
각 칸에서 상하좌우(델타 탐색)에 있는 숫자들과 자신의 숫자를 모두 더해 그 합을 출력하세요.
✅ 조건:
배열을 벗어나는 칸은 무시하고,
자신을 포함한 상하좌우 칸에 있는 숫자의 합을 구합니다.
📥 입력:
첫 줄에 배열 크기 N이 주어집니다. (1 ≤ N ≤ 5)
이후 N개의 줄에 공백으로 구분된 숫자(1~9)들이 주어집니다.
📤 출력:
각 칸마다 구한 합을 공백으로 구분해 출력하세요.
한 줄에 N개씩 출력하세요.
'''
import sys;sys.stdin=open('gpt_practice.txt')

n = int(input())
arr = []
for _ in range(n):
    arr.append(list(map(int,input().split())))

dr=[0,1,0,-1]
dc=[1,0,-1,0]
result = [[0] * n for _ in range(n)]

for r in range(n):
    
    for c in range(n):
        total_sum = 0
        total_sum += arr[r][c]
        for j in range(4):
            nr = r + dr[j]
            nc = c + dc[j]
            if 0<=nr<n and 0<=nc<n:
                total_sum += arr[nr][nc]
        result[r][c] = total_sum
        
for c in result:
    print(*c)