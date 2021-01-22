import binascii

def toString(binaryString):
    return "".join([chr(int(binaryString[i:i + 8], 2)) for i in range(0, len(binaryString), 8)])

with open('/Users/davidfinkelstejn/Desktop/papa_jons_promo.txt', 'r') as file_:
    for row in file_:
        print(hex(int(row, 2))[2:])
        normaltext = bytes.fromhex(hex(int(row, 2))[2:]).decode(encoding="cp1251")
        print(normaltext)
