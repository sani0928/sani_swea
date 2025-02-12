import sys; sys.stdin = open('1221input.txt')

def Planet_Sorting():

    sequence, n = input().split()
    planetlst = list(input().split())
    n = len(planetlst)
    # 행성 이름에 맞는 정수 생성
    planet_dict = {"ZRO":0, "ONE":1, "TWO":2, 
               "THR":3, "FOR":4, "FIV":5, 
               "SIX":6, "SVN":7, "EGT":8, 
               "NIN":9}
    
    # 딕셔너리와 비교해 key에 맞는 value(정수)로 변환
    for i in range(n):
        if planetlst[i] in planet_dict:
            planetlst[i] = planet_dict[planetlst[i]]

    # for i in range(n):
    #     for key, value in planet_dict.items():
    #         if planetlst[i] == key:
    #             planetlst[i] = value
    
    # 딸깍
    planetlst.sort()

    # 다시 value를 key(행성이름)로 변경
    for j in range(n):
        for key, value in planet_dict.items():
            if planetlst[j] == value:
                planetlst[j] = key


    return sequence, planetlst
    


t = int(input())

for _ in range(t):
    sequence, planetlst = Planet_Sorting()
    
    print(sequence)
    print(' '.join(planetlst))

    

    

