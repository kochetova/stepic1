def list_filler(n: int, m: list):
    i = 1
    while i <= n:
        m.append(input().lower())
        i += 1
    return m


w = int(input())
d = []
d = set(list_filler(w, d))

s = int(input())
t = []
list_filler(s, t)

err = set()
for el in t:
    err.update(set(el.split()).difference(d))

for e in err:
    print(e)
