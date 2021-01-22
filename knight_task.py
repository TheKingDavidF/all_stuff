start = complex(0,0)
step1 = complex(2,1)
step2 = complex(1,2)
step3 = complex(-2,1)
step4 = complex(2,-1)
step5 = complex(1,-2)
step6 = complex(-1,2)
step7 = complex(-1,-2)
step8 = complex(-2,-1)
steps = [step1, step2, step3, step4, step5, step6, step7, step8]
[a,b] = [int(aux) for aux in input().split(',')]
finish = complex(a, b)
pos = start
counter = 0
while pos != finish:
    values = [abs(finish - (pos + step)) for step in steps]
    values_aux = []
    for value in values:
        if value == 1:
            value = value*10**10
        values_aux.append(value)
    index = values.index(min(values_aux))
    pos = pos + steps[index]
    counter += 1
    if counter == 10000:
        break

print(counter)