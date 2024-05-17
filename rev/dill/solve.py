import random

LEN = 59
c = [138, 13, 157, 66, 68, 12, 223, 147, 198, 223, 92, 172, 59, 56, 27, 117, 173, 21, 190, 210, 44, 194, 23, 169, 57, 136, 5, 120, 106, 255, 192, 98, 64, 124, 59, 18, 124, 97, 62, 168, 181, 61, 164, 22, 187, 251, 110, 214, 250, 218, 213, 71, 206, 159, 212, 169, 208, 21, 236]

flag = list(range(LEN))

rseed = 'five nights as freddy'
random.seed(rseed)
random.shuffle(flag)
bites = random.randbytes(len(flag))

xorred = list(map(int.__xor__, bites, c))

final = [0] * LEN
for i in range(LEN):
	final[flag[i]] = xorred[i]
final = ''.join(map(chr, final))
print(final)

# amateursCTF{p1ckL3-is_not_the_goat_l4rrY_is_m0R3_\:goat:ed}
