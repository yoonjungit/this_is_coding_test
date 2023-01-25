import sys
N, M, K, *n = map(int, sys.stdin.read().split())
n.sort(reverse= True)
x, y = n[0], n[1]

if x == y :
    ans = x*M
else : 
    u = M //(K+1)
    v = M %(K+1)
    ans = u*(x*K+y) + v*x

print(ans)