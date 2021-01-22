

def twoPluses(grid):
    height = len(grid)
    width = len(grid[0])
    if height == 1 and width == 1:
        if grid[0] == 'B':
            return 0
        else:
            return 1
    pluses = []
    for ii in range(height):
        for jj in range(width):
            if grid[ii][jj] == 'G':
                aux = [ii, jj, 1]
                kk = 1
                while kk <= ii <= height - 1 - kk and kk <= jj <= width - 1 - kk\
                    and grid[ii + kk][jj] == 'G' and grid[ii - kk][jj] == 'G' and\
                    grid[ii][jj + kk] == 'G' and grid[ii][jj - kk] == 'G':
                    aux[2] = aux[2] + 2
                    kk += 1
                pluses.append(aux)
    sort_pluses = sorted(pluses, reverse=True, key=lambda info: info[2])
    # print(sort_pluses)
    areas2 = [0]
    for ii in range(len(sort_pluses)):
        xi = sort_pluses[ii][0]
        yi = sort_pluses[ii][1]
        vali = sort_pluses[ii][2]
        for jj in range(len(sort_pluses)):
            xj = sort_pluses[jj][0]
            yj = sort_pluses[jj][1]
            valj = sort_pluses[jj][2]

            area2 = None
            if ii == jj:
                continue

            if (vali * 2 - 1)**2 <= max(areas2):
                # print('areas: {}; plus_i: {}; plus_j: {}'.format(areas2, sort_pluses[ii], sort_pluses[jj]))
                return max(areas2)
            elif (abs(yi-yj) - 1 >= vali//2 + valj//2) or (abs(xi-xj) - 1 >= vali//2 + valj//2):
                area2 = (vali * 2 - 1) * (valj * 2 - 1)
            elif abs(xi - xj) - 1 >= min(vali//2, valj//2) and abs(yi - yj) - 1 >= min(vali//2, valj//2):
                area2 = (vali * 2 - 1) * (valj * 2 - 1)
            elif (abs(xi - xj) - 1 >= max(vali//2, valj//2) and abs(yi - yj) - 1 >= 0) or \
                    (abs(yi - yj) - 1 >= max(vali//2, valj//2) and abs(xi - xj) - 1 >= 0):
                area2 = (vali * 2 - 1) * (valj * 2 - 1)
            else:
                if yi == yj:
                    if (abs(xi - xj) - 1) % 2 != 0:
                        area2 = ((abs(xi - xj) - 1) // 2 * 4 + 1) * (((abs(xi - xj) - 1) // 2 + 1) * 4 + 1)
                    else:
                        area2 = ((abs(xi - xj) - 1) / 2 * 4 + 1) * ((abs(xi - xj) - 1) / 2 * 4 + 1)
                elif xi == xj:
                    if (abs(yi - yj) - 1) % 2 != 0:
                        area2 = ((abs(yi - yj) - 1) // 2 * 4 + 1) * (((abs(yi - yj) - 1) // 2 + 1) * 4 + 1)
                    else:
                        area2 = ((abs(yi - yj) - 1) / 2 * 4 + 1) * ((abs(yi - yj) - 1) / 2 * 4 + 1)
                elif (abs(xi - xj) - 1) < min(vali//2, valj//2) and (abs(yi - yj) - 1) < min(vali//2, valj//2):
                    if abs(yi - yj) > abs(xi - xj):
                        if vali > valj:
                            area2 = (vali * 2 - 1) * ((abs(xi - xj) - 1) * 4 + 1)
                        else:
                            area2 = (valj * 2 - 1) * ((abs(xi - xj) - 1) * 4 + 1)
                    else:
                        if vali > valj:
                            area2 = (vali * 2 - 1) * ((abs(yi - yj) - 1) * 4 + 1)
                        else:
                            area2 = (valj * 2 - 1) * ((abs(yi - yj) - 1) * 4 + 1)
                elif abs(xi - xj) - 1 < min(vali//2, valj//2):
                    area2 = max(((abs(xi-xj)-1)*4+1)*max(vali*2 - 1, valj*2 - 1), ((abs(yi-yj)-1)*4+1)*min(vali*2 - 1, valj*2 - 1))
                    print('yi: {}, yj {}, xi: {}, xj {}, vali: {}, valj: {} hui: {}'.format(yi, yj, xi, xj, vali, valj, area2))
                elif abs(yi - yj) - 1 < min(vali//2, valj//2):
                    area2 = max(((abs(xi-xj)-1)*4+1)*min(vali*2 - 1, valj*2 - 1), ((abs(yi-yj)-1)*4+1)*max(vali*2 - 1, valj*2 - 1))
            # if area2 < 0:
                # print(ii, jj, area2)
            areas2.append(area2)


    # print('areas: {}; plus_i: {}; plus_j: {}'.format(areas2, sort_pluses[ii], sort_pluses[jj]))
    return max(areas2)



grid1 = '''GGGGGG
GBBBGB
GGGGGG
GGBBGB
GGGGGG'''.split('\n')

grid2 = '''BGBBGB
GGGGGG
BGBBGB
GGGGGG
BGBBGB
BGBBGB'''.split('\n')

grid3 = '''GGGGGGGGGG
GGGGGGGGGG
BBBBBGGBGG
BBBBBGGBGG
GGGGGGGGGG
BBBBBGGBGG
GGGGGGGGGG
BBBBBGGBGG
GGGGGGGGGG'''.split('\n')


grid4 = '''GGGGGGGG
GBGBGGBG
GBGBGGBG
GGGGGGGG
GBGBGGBG
GGGGGGGG
GBGBGGBG
GGGGGGGG'''.split('\n')


grid5 = '''BBGGBBGBBGBBG
BBGGBBGBBGBBG
GGGGGGGGGGGGG
BBGGBBGBBGBBG
GGGGGGGGGGGGG
BBGGBBGBBGBBG
BBGGBBGBBGBBG
GGGGGGGGGGGGG
BBGGBBGBBGBBG
GGGGGGGGGGGGG
BBGGBBGBBGBBG'''.split('\n')


grid6 = '''GBGBGGB
GBGBGGB
GBGBGGB
GGGGGGG
GGGGGGG
GBGBGGB
GBGBGGB'''.split('\n')

grid7 = '''GGGGGGGGGGGG
GBGGBBBBBBBG
GBGGBBBBBBBG
GGGGGGGGGGGG
GGGGGGGGGGGG
GGGGGGGGGGGG
GGGGGGGGGGGG
GBGGBBBBBBBG
GBGGBBBBBBBG
GBGGBBBBBBBG
GGGGGGGGGGGG
GBGGBBBBBBBG'''.split('\n')

grid8 ='''BBBGBGBBB
BBBGBGBBB
BBBGBGBBB
GGGGGGGGG
BBBGBGBBB
BBBGBGBBB
GGGGGGGGG
BBBGBGBBB
BBBGBGBBB
BBBGBGBBB'''.split('\n')

grids = [grid1, grid2, grid3, grid4, grid5, grid6, grid7, grid8]
ans = [5, 25, 85, 81, 169, 45, 81, 81]
for ii, grid in enumerate(grids):
    print('grid#_{}:'.format(ii))
    print('my answer: {}'.format(twoPluses(grid)))
    print('Correct answer: {}'.format(ans[ii]))