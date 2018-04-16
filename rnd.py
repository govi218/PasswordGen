import random
import array
import string

heid = open("h.txt", "r");
a1 = array.array('B', 'Govind Mohan')
r = random.randint(0,15)
c = 0

for line in heid:
	word = line.split(' ')
	L = list(word)
	a = list(L[0])
	# print(a)

	if random.randint(0,15) == r:
		c += 1
		r = random.randint(0,15)
		for i in range(min(len(a1), len(a))):
			a1[i] ^= ord(a[i])
res = ""
for i in range(len(a1)):
	if chr(a1[i]) not in string.letters:
		res += random.choice(string.letters)
	else:
		res += chr(a1[i])
print(a1.tostring(), res[:6], c)