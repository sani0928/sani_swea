'''
10 2 + 3 4 + * .의 경우
10과 2를 저장
10 + 2 값을 저장
그 위에 3과 4를 저장
3 + 4 값을 저장
10 + 2 값과 3 + 4 값을 곱셈
결과출력
'''

import sys;sys.stdin=open('11613_input.txt')

t = int(input())
for x in range(1,t+1):
    s = []
    arr = list(input().split())

    try: 
        for i in arr:
                
                if i == '+':
                    b = s.pop()
                    a = s.pop()
                    s.append(a + b)
                elif i == '*':
                    b = s.pop()
                    a = s.pop()
                    s.append(a * b)
                elif i == '-':
                    b = s.pop()
                    a = s.pop()
                    s.append(a - b)
                elif i == '/':
                    b = s.pop()
                    a = s.pop()
                    s.append(a // b)
                elif i == '.': # e = 최종값
                    if len(s) != 1:
                        raise ValueError # s가 하나 남은게 아니면 오류 일으키기
                    else:
                        e = int(s.pop())
                        print(f'#{x}', e)
                        break
                else:
                    s.append(int(i))

    except (ValueError,IndexError): # 빈 리스트 IndexError 예외처리
        print(f'#{x}', 'error')
        continue