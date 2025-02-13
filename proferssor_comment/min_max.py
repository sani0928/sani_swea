T = int(input())

for i in range(1, T+1):
    N = int(input())
    arr = list(map(int,input().split()))

    max_v = arr[0]
    min_v = arr[0] # 최대값과 최소값의 시작을 arr의 첫 원소로 가정
     
    for x in range(N):
        if arr[x] > max_v:
            max_v = arr[x] # arr[x]이 max_v 보다 크면 max_v이 arr[x]로 대체
            
    for y in range(N):
        if arr[y] < min_v: 
            min_v = arr[y] # arr[x]이 min_v 보다 작으면 min_v이 arr[x]로 대체
    

    print(f'#{i} {max_v - min_v}')