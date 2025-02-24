import sys; sys.stdin = open('7465_input.txt')

def dfs(idx):
    global visited, saving
    visited[idx] = True
    saving.append(idx)
    for next in range(1,n+1):
        if not visited[next] and graph[idx][next]:
            dfs(next)
    return saving

t = int(input())
for x in range(1,t+1):
    n,m = map(int,input().split())
    graph = [[False] * (n+1) for _ in range(n+1)]

    for _ in range(m):
        a,b = map(int,input().split())
        graph[a][b] = True
        graph[b][a] = True



    mob = []
    for i in range(1,n+1):
        visited = [False] * (n+1)
        saving = []
        
        mob.append(sorted(dfs(i)))

    result = []
    for val in mob:
        if val not in result:
            result.append(val)
    
    final = len(result)

    print(f'#{x}', final)