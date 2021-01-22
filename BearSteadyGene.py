



def steadyGene(gene):
    nucls = {"C": 0, "G": 0, "A": 0, "T": 0}

    for nucl in gene:
        nucls[nucl] += 1
    wrong_cons = {"C": 0, "G": 0, "A": 0, "T": 0}

    while nucls['C'] != nucls['G'] or nucls['G'] != nucls['A'] or nucls['A'] != nucls['T']:
        max_val = 0
        for key_ in nucls.keys():
            if nucls[key_] > max_val:
                key_max = key_
                max_val = nucls[key_max]
        min_val = nucls[key_max]
        for key_ in nucls.keys():
            if nucls[key_] < min_val:
                key_min = key_
                min_val = nucls[key_min]
        wrong_cons[key_max] += 1
        nucls[key_max] -= 1
        nucls[key_min] += 1


    # print('nucls: {}, wrong consequence: {}'.format(nucls, wrong_cons))


    substring_count = {'A': 0, 'T': 0, 'G': 0, 'C': 0}
    start = 0
    end = 0
    min_len = len(gene)
    len_st = len(gene)

    # scan :
    # 1)increase scan window size(end += 1) while updating counter
    # 2)optimize size (start+=1) while updating counter
    # 3)repeat 1) and 2) until end point reaches(end >= total size)

    while end < len_st:
        if all([substring_count[nucl] >= wrong_cons[nucl] for nucl in wrong_cons.keys()]):
            curr = end - start
            if curr < min_len:
                min_len = curr
            substring_count[gene[start]] -= 1
            start += 1
        else:
            substring_count[gene[end]] += 1
            end += 1

    return min_len













gene1 = 'GAAATAAA'
with open('/Users/davidfinkelstejn/Desktop/testDNA.txt') as file:
    gene2 = file.read()

# start = datetime.now()
result = steadyGene(gene1)
# print('all script duration: {}'.format(datetime.now() - start))
print(result)