
def minimumLoss(price):
    min_losses = 10**10
    price_sorted = sorted(price)
    for ii in range(len(price_sorted)-1):
        if price_sorted[ii+1] - price_sorted[ii] < min_losses and \
                price.index(price_sorted[ii+1]) < price.index(price_sorted[ii]):
            min_losses = price_sorted[ii+1] - price_sorted[ii]

    return min_losses


price1 = [20, 7, 8, 2, 5]
print(minimumLoss(price1))