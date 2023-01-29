import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())
frame = [list(map(int, input())) for _ in range(N)]
visited = [[False]*M for _ in range(N)]
queue = deque()
queue.append((0, 0))

def bfs(x, y) :
    if x + 1 < M :
        if y+1 < N :
            a = frame[x+1][y+1]
            if a == 0 :
                visited[x+1][y+1]=True
                queue.append((x+1,y+1))
        if y-1 >= 0 :
            a = frame[x+1][y-1]
            if a == 0 :
                visited[x+1][y-1]=True
                queue.append((x+1, y-1))
    if x - 1 > 0 :
        if y+1 < N :
            a = frame[x-1][y+1]
            if a == 0 :
                visited[x-1][y+1]=True
                queue.append((x-1,y+1))
        if y-1 >= 0 :
            a = frame[x-1][y-1]
            if a == 0 :
                visited[x-1][y-1]=True
                queue.append((x-1, y-1))

cnt=0
print(queue.popleft())
# while True :
#     print(queue)
#     if queue :
#         (x, y) = queue.popleft()
#         bfs(x, y)
#     else :
#         cnt+=1
#         for i in range(N) :
#             for j in range(M) :
#                 if not visited[i][j] and frame[i][j] == 0 :
#                     queue.append((i, j))
#                     break
#                 if not visited[i][j] and frame[i][j] == 1 :
#                     visited[i][j] = True
#     if visited :
#         print(cnt)
#         break