import itertools
alphabet = "СЛОН"
ar = itertools.product(alphabet, repeat=3)
arl = []
for i in ar:
    arl.append(list(i))
count = 0
for e in arl:
    if e.count('С') == 1:
        count += 1
print(count)