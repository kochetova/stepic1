n = int(input())
m = []
i = 1

while i <= n:
    d = {}
    m.append(input().split())
    i += 1

pos = [0, 0]


def route_creater(arr: list):
    if arr[0] == 'север':
        pos[1] += int(arr[1])
    elif arr[0] == 'юг':
        pos[1] -= int(arr[1])
    elif arr[0] == 'восток':
        pos[0] += int(arr[1])
    elif arr[0] == 'запад':
        pos[0] -= int(arr[1])
    return pos


for pair in m:
    route_creater(pair)

print(' '.join([str(l) for l in pos]))
