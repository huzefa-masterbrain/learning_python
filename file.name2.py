fname = input('enter file:')
if len(fname) < 1:fname = 'file.name'
hand = open(fname)
di = dict()
for lin in hand:
    lin = lin.rstrip()
    wds = lin.split()

    for w in wds:
        if w in di:
            di[w] = di[w] + 1
        else:
            di[w] = 1
            print('**NEW**')
            print(w,di[w])


            #  http://www.py4e.com/book.php