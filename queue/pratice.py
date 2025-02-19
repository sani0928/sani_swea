from collections import deque

q = deque()
for i in range(1,6):
    q.append(i)
j = 2
q.append(q.popleft()-j)
print(q)