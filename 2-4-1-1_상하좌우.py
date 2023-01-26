import sys
N = int(sys.stdin.readline())
order = sys.stdin.readline().split()
x=[1,1]

def move(ord, x) :
    if ord =="R" :
        x[1]+=1
    elif ord=="L" :
        x[1]-=1
    elif ord=="U" :
        x[0]-=1
    else :
        x[0]+=1
    if x[0]>5 or x[1]>5 :
        if x[0]>5 :
            x[0]-=1
        else :
            x[1]-=1
    if x[0]<1 or x[1]<1 :
        if x[0]<1 :
            x[0]+=1
        else :
            x[1]+=1
    return x

for i in order :
    move(i, x)
print(f'{x[0]} {x[1]}')

''' 저렇게 값을 일일이 다 더했다가 빼지말고 임시 변수를 써서 계산한 다음 적용할지 말지를 판단하는게 코드를 더 알아보기 쉬움
def move(ord, x) :
    a, b = x[0], x[1]
    if ord =="R" :
        b+=1
    elif ord=="L" :
        b-=1
    elif ord=="U" :
        a-=1
    else :
        a+=1
    if a not in [1,2,3,4,5] or b not in [1,2,3,4,5] :
        continue
    x = [a, b]
'''