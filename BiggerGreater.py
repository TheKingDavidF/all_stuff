
def biggerIsGreater1(w):
    arr = list(w)
    # Find non-increasing suffix
    i = len(arr) - 1
    while i > 0 and arr[i - 1] >= arr[i]:
        i -= 1
    if i <= 0:
        return "no answer"

    # Find successor to pivot
    j = len(arr) - 1
    while arr[j] <= arr[i - 1]:
        j -= 1
    arr[i - 1], arr[j] = arr[j], arr[i - 1]

    # Reverse suffix
    arr[i:] = arr[len(arr) - 1: i - 1: -1]
    return "".join(arr)


def biggerIsGreater(w):
    if len(w) == 2:
        new_w = w[1] + w[0]
        if new_w > w:
            return new_w
        else:
            return 'no answer'
    elif len(w) < 2:
        return 'no answer'
    else:
        for ii in [len(w) - 1 - x for x in range(len(w))]:
            for jj in reversed(range(ii+1, len(w))):
                new_w = w[:ii] + w[jj] + w[ii+1:jj] + w[ii] + w[jj+1:]
                if new_w > w:
                    return new_w[:ii+1] + ''.join(sorted(new_w[ii+1:]))
        return 'no answer'



tests = '''ab
bb
hefg
dhck
dkhc
lmno
dcba
dcbb
abdc
abcd
fedcbabcd'''.split('\n')

correct_results = '''ba
no answer
hegf
dhkc
hcdk
lmon
no answer
no answer
acbd
abdc
fedcbabdc
'''.split('\n')

for test, result in zip(tests, correct_results):
    print('Input: {};\nmy result: {};\ncorrect result: {};\n'.format(test, biggerIsGreater1(test), result))