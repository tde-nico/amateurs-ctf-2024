import random as random
seed = int('1665663c', 20)
print(seed)
random.seed(seed)

flag = bytearray(open('flag.txt', 'rb').read())
crs = '\r'r'\r''r''\\r'r'\\r\r'r'r''r''\\r'r'r\r'r'r\\r''r'r'r''r''\\r'r'\\r\r'r'r''r''\\r'r'rr\r''\r''r''r\\'r'\r''\r''r\\\r'r'r\r''\rr'
rs = [
    b'arRRrrRRrRRrRRrRr',
    b'aRrRrrRRrRr',
    b'arRRrrRRrRRrRr',
    b'arRRrRrRRrRr',
    b'arRRrRRrRrrRRrRR'
    b'arRRrrRRrRRRrRRrRr',
    b'arRRrrRRrRRRrRr',
    b'arRRrrRRrRRRrRr'
    b'arRrRrRrRRRrrRrrrR',
]
print(crs.encode())


inc = lambda x: bytearray([i + 1 for i in x])
dec = lambda x: bytearray([i - 1 for i in x])

def func(hex):
    for id in range(0, len(hex) - 1, 2):
        hex[id], hex[id + 1] = hex[id + 1], hex[id]
    for list in range(1, len(hex) - 1, 2):
        hex[list], hex[list + 1] = hex[list + 1], hex[list]
    return hex

funcs = [func, inc, dec]
funcs = [random.choice(funcs) for i in range(128)]

def encrypt(arr, ar):
    for r in ar:
        print(r)
        arr = funcs[r](arr)
        print('arr', arr)
    return arr

def func2(arr, ar):
    print('ar', ar)
    ar = int(ar.hex(), 17)
    print('ar 17', ar)
    for r in arr:
        #print('r 35', r)
        ar += int(r, 35)
    return bytes.fromhex(hex(ar)[2:])

print(flag)
final_flag = encrypt(flag, crs.encode())
print(rs, final_flag)
final_flag = func2(rs, final_flag)

print(final_flag.hex())
