fname = input('enter file:')
if len(fname) < 1 : fname = 'collection and dictionries.txt'
hand = open(fname)

for lin in hand:
    lin = lin.rstrip()
    print(lin)
    wds = lin.split()
    print(wds)
    for w in wds:
        print(w)
