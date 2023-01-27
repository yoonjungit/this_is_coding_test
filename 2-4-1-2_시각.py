N = int(input())
time_limit = (N+1)*60*60
time = [0,0,0]
cnt = 0
while True :
    time[2]+=1
    if time[2] >= 60 :
        time[1]+=1
        time[2] = 0
    if time[1] >= 60 :
        time[0]+=1
        time[1] = 0
    for t in time :
        if '3' in str(t) :
            cnt+=1
            break
    if time == [N, 59, 59] :
        break
print(cnt)

''' 60을 검증하지말고 for문으로 대체, 어차피 브루트포스라 걸리는 시간은 같음, 그리고 문자열은 +로 합치기
hour, min, sec = 0,0,0
for hour in range(N+1) :
    for min in range(60) :
        for sec in range(60) :
            if '3' in str(hour)+str(min)+str(sec) :
                cnt+=1
'''