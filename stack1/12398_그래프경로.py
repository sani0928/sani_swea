import sys;sys.stdin=open('12398_input.txt')

def dfs(idx):
    global visited
    visited[idx] = True
    print(idx, end=' ')
    for next in range(1,v+1):
        if not visited[next] and graph[idx][next]:
            dfs(next)
    
    return visited



t=int(input())
for x in range(1,t+1):
    v,e = map(int,input().split())
    graph = [[False]*(v+1) for _ in range(v+1)]
    visited = [False] * (v+1)
    # saving = []
    for _ in range(e):
        a, b = map(int,input().split())
        graph[a][b] = True
        # graph[b][a] = True # 무방향
    
    s,g = map(int,input().split())
    
    for c in graph:
        print(*c)
    dfs(s)
    if visited[g] is True:
        print(f'#{x}', 1)
    else:
        print(f'#{x}', 0)