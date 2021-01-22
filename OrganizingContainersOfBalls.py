
def check_possible(M):
    tot_t = []
    tot_c = []
    for ii in range(len(M)):
        sum_t_i = 0
        sum_c_i = 0
        for jj in range(len(M)):
            sum_t_i += M[ii][jj]
            sum_c_i += M[jj][ii]
        tot_t.append(sum_t_i)
        tot_c.append(sum_c_i)

        tot_c.sort()
        tot_t.sort()

    if tot_c == tot_t:
        return 'Possible'
    else:
        return 'Impossible'



with open('/Users/davidfinkelstejn/Desktop/test_containers.txt') as file:
    matrixes = []
    aux_list = []
    for row in file:
        row_list = list(map(int, row.split()))
        if len(row_list) > 1:
            aux_list.append(row_list)
        elif len(row_list) == 1:
            if aux_list:
                matrixes.append(aux_list)
                aux_list = []



correct_ans = '''Possible
Possible
Possible
Impossible
Possible
Impossible
Possible
Possible
Possible
Possible
'''.split()
for ii, M in enumerate(matrixes):
    for row in M:
        print(row)
    print('My answer: {}'.format(check_possible(M)))
    print('Correct answer: {}'.format(correct_ans[ii]))
    print('\n\n')
