
S = input().lower()
M = list(set(S))
string_cnt = []
for i in M:
    string_number = S.count(i)
    string_cnt.append(string_number)

if string_cnt.count(max(string_cnt)) >= 2:
    print('?')
else:
    max = M[string_cnt.index(max(string_cnt))]
    print(max.upper())