import sys
N, M = map(int, sys.stdin.readline().split())
cards = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

for x in range(N) :
    y = min(cards[x])
    cards[x]=y

print(max(cards))

'''시간을 더 줄이려면 max를 하지말고, for문에서 최댓갑을 찾음'''
