import sys
N, M = map(int, sys.stdin.readline().split())
x, y, direction = map(int, sys.stdin.readline().split())
Map = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
been = [(x, y)]
went = 1
def direct(d) :
    d-=1
    if d == -1 :
        d = 3
    return d

def move(d, a, b) :
    global went
    u, v = a, b
    if d %2 == 0 :
        if d == 0 :
            u-=1
        else :
            u+=1
    else :
        if d == 1 :
            v+=1
        else :
            v-=1
    if u>=N or u<0 or v>=M or v<0 :
        return None
    if Map[u][v]==1:
        return None
    if (u, v) in been :
        return None
    a, b = u, v
    been.append((a, b))
    went+=1
    return [a, b]

def go_back(d, a, b) :
    u, v = a, b
    if d %2 == 0 :
        if d == 0 :
            u+=1
        else :
            u-=1
    else :
        if d == 1 :
            v-=1
        else :
            v+=1
    if u>=N or u<0 or v>=M or v<0 :
        return None
    if Map[u][v]==1:
        return None
    if (u, v) in been :
        return None
    a, b = u, v
    return [a, b]

back = 0
while True :
    direction = direct(direction)
    go = move(direction, x, y)
    if go == None :
        back +=1
        if back == 4:
            b = go_back(direction, x, y)
            if b == None :
                break
    else :
        x, y = go[0], go[1]
        back = 0
    
print(went)