knight = input()
column, row = int(ord(knight[0]))-int(ord('a'))+1, int(knight[1])
m=0

def move_2(x, y) :
    if 8-x>=2 :
        move_1(y)
    if x-1>= 2 :
        move_1(y)
            
def move_1(y) :
    global m
    if y-1 >= 1 :
        m+=1
    if 8-y >= 1 :
        m+=1

move_2(column, row)
move_2(row, column)
print(m)

'''
책에서는 애초에 움직임을 튜플로 저장해서 (-2, 1), (2, -1) 등 
이거를 하나씩 for문 돌려서 할 수 있는지 검증을 하는데 무엇이 더 좋은 방법인지는 모르겠다!'''