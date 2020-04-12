with open('/Users/igumnyash/Downloads/dataset_3380_5.txt') as file:
    lst = file.readlines()

def dist_writer(arr: list, d: dict):
    cl = int(arr[0])
    h = int(str(arr[2]).replace('\n', ''))
    if cl in d:
        d[cl].append(h)
    else:
        d[cl] = [h]
    return d

d = {}
for s in lst:
    dist_writer(s.split('\t'), d)

dd = {}
for i in range(1, 12):
    dd.setdefault(i, '-')


for k, v in d.items():
    if k in dd:
        dd[k] = sum(v) / len(v)

for k, v in sorted(dd.items()):
    print(k, v)
