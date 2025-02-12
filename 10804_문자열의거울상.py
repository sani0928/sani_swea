import sys; sys.stdin = open('10804input.txt')

t = int(input())

mirror_dict = {'b':'d', 'd':'b', 'q':'p', 'p':'q'}

def mirror(str):
    

    n = len(str)

    for i in range(n//2):
        str[i],str[n-1-i] = str[n-1-i],str[i]
    
    for j in range(n):
        if str[j] in mirror_dict:
            str[j] = mirror_dict[str[j]]

    return str

for x in range(1, t+1):
    print(f'#{x}', ''.join(mirror(list(input()))))