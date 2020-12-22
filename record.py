scores1=[10, 5, 20, 20, 4, 5, 2, 25, 1]
scores2=[3, 4, 21, 36, 10, 28, 35, 5, 24, 42]


def RecBreak(N):
	mincount=0
	maxcount=0
	min=N[0]
	max=N[0]
	for i in N:
		if min>i:
			min=i
			mincount+=1	
		if max<i:
			max=i
			maxcount+=1
	print(maxcount,mincount)
	return maxcount,mincount


RecBreak(scores1)

RecBreak(scores2)