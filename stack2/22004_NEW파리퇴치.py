import sys;sys.stdin=open('22004_input.txt')

t=int(input())
for x in range(1,t+1):
    n,h,w = map(int,input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]
    
    count = 0
    max_count = 0

    r,c = 0,0
    dr = [-1,1] #위,아래
    dc = [1,-1] #왼쪽,오른쪽

    lst = []
    lst_2 = []

    def right(arr,r,c):
        global lst

        nc = c + dc[0]*1
        lst.append(arr[r][nc])
        
        down(arr,r,nc)
        return lst
        


    def down(arr,r,c):
        global lst

        nr = r + dr[1]*1
        lst.append(arr[nr][c])
        
        left(arr,nr,c)
        return lst


    def left(arr,r,c):
        global lst

        nc = c + dc[1]*1
        lst.append(arr[r][nc])

        up(arr,n,nc)
        return lst


    def up(arr,r,c):
        global lst

        nr = r + dr[0]*1
        lst.append(arr[nr][c])
        return lst


        
    result = left(arr,r,c)
    print(f'#{x}',result)




             

        
