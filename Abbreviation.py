



def abbreviation1(a, b):
    if len(a) < len(b):
        return "NO"
    j = len(b)-1
    res = []
    n = -1 * len(a)
    for i in range(-1, n-1, -1):
        if a[i].upper() == b[j] and j >= 0:
            res.append(a[i])
            j -= 1
        elif a[i].isupper() and a[i].lower() in res:
            if a[i].lower() == res[-1]:
                res.remove(a[i].lower())
                res.append(a[i])
        elif a[i].isupper():
            return "NO"
    if len(res) == len(b):
        return "YES"
    else:
        return'NO'

def abbreviation(a, b):
    m, n = len(a), len(b)
    dp = [[False]*(m+1) for _ in range(n+1)]
    dp[0][0] = True
    for ii in range(n+1):
        for jj in range(m+1):
            if ii == 0 and jj != 0:
                dp[ii][jj] = dp[ii][jj-1] and a[jj-1].islower()
            elif ii != 0 and jj != 0:
                if a[jj-1] == b[ii-1]:
                    dp[ii][jj] = dp[ii-1][jj-1]
                elif a[jj-1].upper() == b[ii-1]:
                    dp[ii][jj] = dp[ii - 1][jj - 1] or dp[ii][jj-1]
                elif a[jj - 1].islower():
                    dp[ii][jj] = dp[ii][jj - 1]

    return "YES" if dp[n][m] else "NO"





a ='daBcd'
b= 'ABC'

a2 ='beFgH'
b2 = 'EFG'

a3 = '''rReRRREreEreERRrreeeRrrrErReerreererEreEEseeEeErreEEereeerrerREreeeeerreeerrEEEReErrEeeeeREesrRerereRrreRreRRrreeEeEeERerrreweRrrEREEerRrrreRRrrEREreEerrrerrRerReeeerrErrreREreerrrRrreeereEseErreerrEreererRreereerrreeRrreEreerreRRErRERereEEerReReeEERrEEeeEeEeereeReeeeeReEerEREReseereRereEeeerEreEEereerEeEesrerrRerrererrerrReERrreeereeeeRerrEeeEerreRRrrRErseeErrEeeeerreeRErrRrRerrrrrerRErrerEeeeerrreerrreErrerEeeeeRRererrEReEeeererErErErRerrerErRrrRRrerrErrerrreErerrrreerreERReRerererErreRrererreRrReEERRereeeErEreeREEeeeErReRrreerRrRrreeRrRrEEEEereeerErrrerreErErrRRrreErReReRerrrerEereRreerererReERREeeeeeEeRerRerReeSrreesreeeeREeErresreeReeRrerrrrererrrrrreerrrrrrRREEerrerrErRRRereeerrREEreeEeerrEeeereeerReRerrrEEerrEEReEeerErerRrErSerErRRreERrerEeeerereEreEeerrREEEReereeRErerRrrrReeReEERrrerereereeErEEREeRSreRrRrreerrrReErReErerreerrrRrseererrerererrrreEeeRReRrerreeRerrRRerRPeeRerrreeRrrREereeEErererrRRRererrrerEEerrRrrReerRereeEerrsREEReEerEreEErrrsErreErereeerrrrRrrEeeErReEeReEeeeeEe'''
b3 = '''RRRREERERREERRERREEEEEEEEEERRREREEERRREEEEEEREESRRRRRRREEERRRREERRERREREEREREEERERRREERRRRESERERRERRRREEEEERREREREEEERREEERREEEEEEREEEREEERERERREEREREEEEEERRREREERRREERRRRRREEREEEERERREREREERRREEREREERREREREEREERERERRRERERERERRRREERRRERERRRERRREERREEEEEREREEREEEERRRREERRRRERRREEEERERERERRRERRREEREEREERERREEEERRRESRESEREESRERRRRRRRERRRREEERERRRRERREEEEEEEEERRRRRREREEREEEERRESRRRRRREREEEEREERREEERRERRRREEERREEEEEERRSRRRERRERREERREERRRREERRRRRRRRRRPRRREEEEEEERRREEERRRRRERREEREEEEEREREEEERREEEREEREE'''
print(abbreviation(a3, b3))