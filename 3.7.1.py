n = int(input())
d = {}
i = 1
while i <= n:
    m = input().split(';')
    for t in range(0, len(m), 2):
        if m[t] in d:
            d[m[t]][0] += 1
        else:
            d[m[t]] = [1, 0, 0, 0, 0]
        if int(m[t + 1]) > int(m[t - 1]):
            d[m[t]][1] += 1
            d[m[t]][4] += 3
        elif int(m[t + 1]) == int(m[t - 1]):
            d[m[t]][2] += 1
            d[m[t]][4] += 1
        else:
            d[m[t]][3] += 1
            d[m[t]][4] += 0
    i += 1
for key in d:
    print(key + ':', end='')
    for i in d[key]:
        print(i, end=' ')
    print()
