import sys
N, K = map(int, sys.stdin.readline().split())
cnt = 0
while K < N :
    K*=K
    cnt+=1
if cnt != 0 :
    cnt+=1
print(cnt+N-K)