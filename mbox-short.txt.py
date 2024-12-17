

han = open('mbox-short.txt')
for line in han :
    line = line .rstrip()
    wrd = line.split()
    if wds[0]! = 'from':
        continue
        print(wds[2])

han = open('mbox-short.txt')
for line in han:
    line = line.rstrip()
    print('line:'line)
    wds = line.split()
    print('words:',wds)
    if len (wds) < 1:
        continue
        if wds[0]! = 'from':
            print('ignore')
            continue
            print(wds[2])

 han = open('mbox-short.txt')
 for line in han:
     line = line.rstrip()
     wds = line.split()
     if len(wds) < 3:
         continue
         if wds[0]!='from':
             continue
             print(wds[2])

han = open('mbox-short.txt')
for line in han :
    line = line.split()
    wds = line.split()
    # giadian in a compound statament
    if len(wds) < 3 or wds[0]! ='from':
        continue
        print(wds[2])
