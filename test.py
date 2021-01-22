
xi, yi, vali = 6, 3, 7
xj, yj, valj = 3, 2, 5
areas2 = [0]

bol_res = abs(xi - xj) - 1 >= min(vali//2, valj//2) and abs(yi - yj) - 1 >= min(vali//2, valj//2)

print(bol_res)