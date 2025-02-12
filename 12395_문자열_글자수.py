import sys; sys.stdin = open('12395input.txt')

# s1 = input()
# s2 = input()
# print(s1, s2)
# print(s1[0] == s2[2])

t = int(input())
for x in range(1,t+1):
    str1 = input()
    str2 = input()

    lst = []
    counts = 0
    for i in str1:
        for j in str2:
            if i == j:
                lst.append(i)
                print(lst)
        
    # counts = {}
    # for value in lst:
    #     if value in counts:
    #         counts[value] += 1
    #     else:
    #         counts[value] = 1
    # all_values = counts.values()
    # print(f'#{x}', max(all_values))