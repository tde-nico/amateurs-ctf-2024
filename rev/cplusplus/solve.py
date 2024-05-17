from string import printable

output = [816696039, 862511530, 897431439, 341060728, 173157153, 31974957, 491987052, 513290022, 463763452, 949994705, 910803499, 303483511, 378099927, 773435663, 305463445, 656532801, 655150297, 28357806, 69914739, 213536453, 962912446, 458779691, 598643891, 94970179, 732507398, 792930123, 216371336, 680163935, 397010125, 693248832, 926462193, 419350956, 594922380, 944019434, 93600641, 116339550, 373995190, 558908218, 700841647, 703877327, 665247438, 690373754, 35138387, 389900716, 625740467, 682452898, 894528752, 603308386, 442640217, 15961938, 573068354]
p = 1000000007


out = 0
for i in range(256):
	for j in range(256):
		s = 97 % p # b'a' % p  ->  first char of flag format
		m = (s * i) % p
		out = pow(m, j, p)
		if out == output[0]:
			print('rands:', i, j, end='\n\n')
			break
	else:
		continue
	break
else:
	print('not found')
	exit()


rands = [i, j] # [237, 41]
out = 0
flag = []
while len(flag) == 0 or flag[-1] != '}':
	for c in printable:
		c_ = ord(c)
		s = (out + c_) % p
		m = (s * rands[0]) % p
		o = pow(m, rands[1], p)
		if o == output[len(flag)]:
			flag.append(c)
			print(''.join(flag))
			out = o
			break
	else:
		print('not found')
		exit()

print()
print(''.join(flag))

# amateursCTF{r/programminghorror/comments/18x7vk9/}

# https://www.reddit.com/r/programminghorror/comments/18x7vk9/why_does_everyone_keep_telling_me_to_use_c/
