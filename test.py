# def build(se):
# 	r = {}
# 	for s in se:
# 		b = s
# 		for w in s.split(' '):
# 			if not b.get(w):
# 				b[w] = {}
# 			b = b[w]
# 	return r


# t = print(build(["Hello world", "Hello there"]))




# def f1(a):
# 	if a ==0:
# 		return 1
# 	return a * f1(a-1)



# f2 = lambda a, b: abs(2* a-3*b)

# print(f1(f2(2, 3)))


def ha(n):
	h1 = False
	h2 = False

	for i in n:
		h1 = i > 0
		h2 = i < 0
	return (h1, h2)

print(ha([0, 1,2]))
print(ha([0, -1,-2]))
print(ha([-1, 0, -1]))
print(ha([]))