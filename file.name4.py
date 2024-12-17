fname = input('enter file:')
if len(fname) < 1:fname = 'file.name'
hand = open(fname)
di = dict()
for lin in hand:
    lin = lin.rstrip()
    wds = lin.split()

    for w in wds:
        oldcount = di.get(w,o)
        print(w,'old' , oldcount)
        newcount = oldcount + 1
        di:[w] = newcount
        print(w,'new',newcount)
        print(di)



            #  http://www.py4e.com/book.php