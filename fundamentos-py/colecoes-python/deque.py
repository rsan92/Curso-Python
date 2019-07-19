from collections import deque

deq = deque('Rafael')
print(deq)

deq.append('X')
deq.appendleft('Z')
print(deq)

deq.popleft()
deq.pop()
print(deq)


