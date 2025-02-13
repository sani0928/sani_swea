import sys;sys.stdin = open ('3499_input.txt')

def 셔플(card, n):

    result = []
    if n % 2 == 0: # n이 짝수일 때
        lst1 = card[0:n//2]
        lst2 = card[n//2:n]
    
        for i in range(n//2):
            result.append(lst1[i])
            result.append(lst2[i])
    
    else:  # n이 홀수일 때
        lst1 = card[0:n//2+1]
        lst2 = card[n//2+1:n]

        result.append(lst1[0])

        for j in range(1,n//2+1):
            result.append(lst2[j-1])
            result.append(lst1[j])
            

    return result

t = int(input())
for x in range(1, t+1):
    n = int(input())
    s = input().split()
    print(f'#{x}', *(셔플(s, n)))