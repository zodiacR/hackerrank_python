n = raw_input()
l = [[raw_input(), float(raw_input())] for i in range(int(n))]

from operator import itemgetter

l.sort(key=itemgetter(1))

newlist = []
deli = l[0][1]
newlist.append([])
k = 0

for i in l:
    if deli == i[1]:
        newlist[k].append(i[0])
    else:
        k += 1
        deli = i[1]
        newlist.append([])
        newlist[k].append(i[0])
newlist[1].sort()        
for i in newlist[1]:
    print i
