import re

def gridSearch1(G, P):
    lineChecks = 0
    for i in range(len(G[0])-len(P[0])+1):
        for j in range(len(G)-len(P)+1):
            if G[j][i:i+len(P[0])] == P[0]:
                for x in range(1, len(P)):
                    if G[j+x][i:i+len(P[0])] == P[x]:
                        lineChecks += 1
                        if lineChecks == len(P) - 1:
                            return "YES"
                    else:
                        lineChecks = 0
    return "NO"

def gridSearch(G, P):
    for ii, row in enumerate(G):
        if P[0] in row:
            first_str = re.search(P[0], row)
            jj = ii + 1
            kk = 1
            counter = 1
            start = first_str.span()[0]
            while G[jj][start:start+len(P[kk])] == P[kk]:
                counter += 1
                kk += 1
                jj += 1
                if counter == len(P):
                    return 'YES'
    return 'NO'


G1 = '''7283455864
6731158619
8988242643
3830589324
2229505813
5633845374
6473530293
7053106601
0834282956
4607924137'''.split('\n')

P1 = '''9505
3845
3530'''.split('\n')

G2 = '''400453592126560
114213133098692
474386082879648
522356951189169
887109450487496
252802633388782
502771484966748
075975207693780
511799789562806
404007454272504
549043809916080
962410809534811
445893523733475
768705303214174
650629270887160'''.split('\n')

P2 = '''99
99'''.split('\n')

G3='''111111111111111
111111111111111
111111111111111
111111011111111
111111111111111
111111111111111
101010101010101
'''.split('\n')

P3 = """11111
11111
11111
11110
""".split('\n')
print(gridSearch(G2, P2))

