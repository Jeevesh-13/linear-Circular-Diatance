import sys

f = open(sys.argv[1], 'r')
f1 = open(sys.argv[2], 'w')

for inp in f.readlines():
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    ldis, cdis = 0, 0
    s1, s2 = map(str,inp.split())

    for i in range(len(s1)):
        ld = abs(alpha.index(s1[i])-alpha.index(s2[i]))
        cd1 = abs(alpha.index(s1[i])-(26 + alpha.index(s2[i])))
        cd2 = abs(alpha.index(s2[i])-(26 + alpha.index(s1[i])))
        ldis += ld
        cdis += min((cd1, cd2, ld))
        
    ww = str(ldis)+" "+str(cdis)+'\n'
    f1.write(ww)
