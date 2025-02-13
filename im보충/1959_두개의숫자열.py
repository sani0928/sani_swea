import sys;sys.stdin = open('1959_input.txt')

t = int(input())

for x in range(1, t+1):
    Ai_len,Bj_len = map(int, input().split())
    Ai = list(map(int, input().split()))
    Bj = list(map(int, input().split()))
    max_val = 0

    # 총 9번의 반복 시행
    if Ai_len > Bj_len:
        
        for j in range(Ai_len-Bj_len+1): 
            temp_calcul = 0      
            for i in range(Bj_len):      
                temp_calcul += Bj[i]*Ai[i+j]
            if temp_calcul > max_val:
                max_val = temp_calcul
    
    elif Ai_len < Bj_len:   
        for j in range(Bj_len-Ai_len+1):
            temp_calcul = 0      
            for i in range(Ai_len):
                temp_calcul += Ai[i]*Bj[i+j]
            if temp_calcul > max_val:
                max_val = temp_calcul

    else: # ai_len == bj_len
        for j in range(Bj_len): 
            temp_calcul += Ai[i]*Bj[i]
        if temp_calcul > max_val:
            max_val = temp_calcul
    
    print(f'#{x}',max_val)