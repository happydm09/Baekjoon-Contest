N = int(input())
egg_plant = input().split()
m, k = map(int, input().split())

for i in range(m):
    h = list(map(int, input().split()))
    for e in range(len(h)):
        n = egg_plant[h[e] - 1]
        h[e] = n
    if str(h).find('P') == -1:
        print('W')
        break
else:
    print('P')
