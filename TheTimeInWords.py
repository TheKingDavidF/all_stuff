
def timeInWords(h, m):
    numbers = {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six',
             7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten', 11: 'eleven', 12: 'twelve',
               13: 'thirteen', 14: 'fourteen', 15: 'fifteen', 16: 'sixteen', 17: 'seventeen',
               18: 'eighteen', 19: 'nineteen', 20: 'twenty', 30: 'thirty', 40: 'forty', 50: 'fifty'}
    if m == 0:
        return numbers[h] + " " + "o' clock"
    if m == 1:
        return 'one minute past' + ' ' + numbers[h]
    elif m < 30:
        if m == 15:
            return 'quarter past' + ' ' + numbers[h]
        if m <= 20:
            return numbers[m] + ' ' + 'minutes past' + ' ' + numbers[h]
        else:
            return numbers[m // 10 * 10] + ' ' + numbers[m % 10] + ' ' + 'minutes past' + ' ' + numbers[h]
    elif m == 30:
        return 'half past' + ' ' + numbers[h]
    else:
        if m == 45:
            return 'quarter to' + ' ' + numbers[h + 1]
        else:
            m = 60 - m
            if m == 1:
                return 'one minute to' + ' ' + numbers[h + 1]
            elif m <= 20:
                return numbers[m] + ' ' + 'minutes to' + ' ' + numbers[h + 1]
            else:
                return numbers[m // 10 * 10] + ' ' + numbers[m % 10] + ' ' + 'minutes to' + ' ' + numbers[h + 1]


print(timeInWords(5, 1))