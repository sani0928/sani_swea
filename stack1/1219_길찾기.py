import sys; sys.stdin = open('1219_input.txt')

def dfs(idx):
    global visited, tracking_lst
    visited[idx] = True
    tracking_lst.append(idx)
    for next in range(1,100):
        if not visited[next] and graph[idx][next]:
            dfs(next)

    return tracking_lst


for x in range(1, 11):
    x, m = map(int,input().split())
    temp = list(map(int,input().split()))

    graph = [[False] * 100 for _ in range(100)]
    visited = [False] * 100
    tracking_lst = []

    for i in range(0,len(temp),2):
        a = temp[i]
        b = temp[i+1]
        graph[a][b] = True
        # graph[b][a] = True
    

    if 99 in dfs(0):
        print(f'#{x}', 1)
    else:
        print(f'#{x}', 0)