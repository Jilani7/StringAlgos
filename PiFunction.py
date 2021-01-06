def PiFunction(p):
	l = len(p)
	pi = [0]
	j = 0
	for i in range(1,l):
		while(j > 0 and p[j] != p[i]):
			j = pi[j-1]
		if (p[j] == p[i]):
			j = j + 1
		pi.append(j)
