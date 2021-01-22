

def non_divisible_subset(k, s):
    res = []
    for ii in range(len(s)):
        new_s = [s[jj] for jj in range(len(s)) if jj != ii]
        if if_sum_div_k(k, s[ii], new_s):
            res.append(len(s))
        else:
            res.extend(non_divisible_subset(k, new_s))

    return res



def if_sum_div_k(k, comp_el, s):
    for el in s:
        if (comp_el + el) % k == 0:
            return 0
    return 1

def div(k, num):
    return num%k

def by_remainders(k, s):
    rem_list = list(map(div, [k]*len(s), s))
    counter = 0
    if rem_list.count(0):
        counter += 1
    for rem in range(1, k//2+1):
        if rem == k - rem:
            if rem_list.count(rem):
                counter += 1
        else:
            if rem_list.count(rem) >= rem_list.count(k-rem):
                counter += rem_list.count(rem)
            else:
                counter += rem_list.count(k - rem)
    return counter




print(by_remainders(4, list(map(int,'1 2 3 4 5 6 7 8 9 10'
                                            .split()))))

