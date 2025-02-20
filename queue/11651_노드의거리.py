import sys;sys.stdin=open('11651_input.txt')
from collections import deque

def bfs(s):
    visited = [0] * (v+1)
    D = [0] * (v+1) # 최단 거리
    P = [0] * (v+1)
    q = deque()


    q.append(s) # 시작 위치 저장
    D[s] = 0
    visited[s] = 1 # 방문 위치 저장
    while q: #큐가 비워질 때까지 반복
        t = q.popleft() #FIFO
        visited[s] = 1
        for w in G[t]:
            if not visited[w]: # 방문한 적이 없다면
                q.append(w) # 큐에 삽입
                visited[w] = 1
                D[w] = D[t] + 1
                P[w] = t
    print(f'#{x}', D[g])

t = int(input())
for x in range(1,t+1):
    v, e = map(int, input().split())

    arr = []
    for _ in range(e):
        arr.extend(map(int,input().split()))
    s, g = map(int,input().split())

    G = [[] for _ in range(v+1)]
    for i in range(0, e*2, 2): # 인접 노드 정리
        a,b = arr[i], arr[i+1]
        G[a].append(b)
        G[b].append(a)

    bfs(s)