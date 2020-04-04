f_ln = input()
s_ln = input()
to_encrypt = input()
to_decrypt = input()

d = {}

for i in range(len(f_ln)):
    d[f_ln[i]] = s_ln[i]

is_encrypted = ''
for en in range(len(to_encrypt)):
    if to_encrypt[en] in d.keys():
        is_encrypted += d[to_encrypt[en]]

dd = {}
for k, v in d.items():
    dd[v] = k

is_decrypted = ''
for de in range(len(to_decrypt)):
    if to_decrypt[de] in dd.keys():
        is_decrypted += dd[to_decrypt[de]]

print(is_encrypted)
print(is_decrypted)
