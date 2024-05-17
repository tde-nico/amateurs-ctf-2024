c = '5915f8ba06db0a50aa2f3eee4baef82e70be1a9ac80cb59e5b9cb15a15a7f7246604a5e456ad5324167411480f893f97e3'


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


inc = lambda x: bytearray([i + 1 for i in x])
dec = lambda x: bytearray([i - 1 for i in x])

def func(enc):
	for list in range(1, len(enc)-1, 2):
		enc[list], enc[list + 1] = enc[list + 1], enc[list]
	for id in range(0, len(enc) - 1, 2):
		enc[id], enc[id + 1] = enc[id + 1], enc[id]
	return enc


funcs = [
	'func',	'func',	'dec',	'inc',	'inc',	'dec',	'func',	'func',
	'dec',	'dec',	'dec',	'dec',	'inc',	'func',	'inc',	'inc',
	'func',	'func',	'func',	'dec',	'dec',	'func',	'inc',	'func',
	'func',	'func',	'inc',	'inc',	'func',	'func',	'dec',	'dec',
	'func',	'func',	'func',	'func',	'inc',	'func',	'dec',	'dec',
	'dec',	'dec',	'func',	'inc',	'dec',	'inc',	'dec',	'func',
	'inc',	'inc',	'inc',	'func',	'func',	'dec',	'dec',	'func',
	'func',	'func',	'func',	'dec',	'dec',	'inc',	'func',	'dec',
	'inc',	'dec',	'inc',	'func',	'dec',	'dec',	'func',	'dec',
	'func',	'func',	'func',	'dec',	'inc',	'func',	'dec',	'dec',
	'dec',	'inc',	'inc',	'dec',	'inc',	'inc',	'inc',	'inc',
	'func',	'func',	'dec',	'inc',	'inc',	'inc',	'inc',	'func',
	'inc',	'dec',	'inc',	'dec',	'func',	'inc',	'func',	'inc',
	'dec',	'inc',	'inc',	'func',	'inc',	'func',	'dec',	'inc',
	'dec',	'dec',	'dec',	'func',	'func',	'dec',	'inc',	'inc',
	'dec',	'inc',	'dec',	'func',	'dec',	'func',	'inc',	'dec'
]

dec_funcs = []
for fun in funcs:
	if fun == 'func':
		dec_funcs.append('func')
	elif fun == 'inc':
		dec_funcs.append('dec')
	elif fun == 'dec':
		dec_funcs.append('inc')

order = [int(b) for b in crs.encode()][::-1]

ordered_dec_funcs = []
for fun in order:
	ordered_dec_funcs.append(dec_funcs[fun])


def base17_to_base10(enc):
	big = 0
	m = 1
	while m >= 1:
		m = enc / (17 ** big)
		big += 1
	big -= 2
	done = []
	while big > 0:
		num = int(enc / (17 ** big))
		enc -= (17 ** big) * (num)
		done.append(hex(num)[2:])
		big -= 1
	if len(done) % 2 != 0:
		done.append(hex(enc)[2:])
	done = ''.join(done)
	a = bytearray.fromhex(done)
	return a


def inv_func2(enc: str):
	enc = int(enc, 16)
	for r in rs:
		enc -= int(r, 35)
	enc = base17_to_base10(enc)
	return enc


final_flag = inv_func2(c)

for fun in ordered_dec_funcs:
	if fun == 'func':
		final_flag = func(final_flag)
	elif fun == 'inc':
		final_flag = inc(final_flag)
	elif fun == 'dec':
		final_flag = dec(final_flag)


print(final_flag)
