di = dict()
for lin in hand:
    lin = lin.rstrip()
    wds = lin.split()
    for w in wds:
        # idom:retrieve/create/update counter
    di[w] = di.get(w,o) + 1
    # print(di)
    # now we want to find the most common word
    for k,v in di.items():
        print(k,v)

        largest = -1
        for k,v in di.items():
            print(k,v)
            if v > largest:
                largest = v
                theword = k
                print('done' , theword , largest)