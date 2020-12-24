n=6
k=3
ar=[1,3,2,6,1,20]


def divisibleSumPairs(n, k, ar):
	s=2
	count=0
	arr=[]
	#arr=[ar[i:i+s] for i in range(0,len(ar)-1+s)]
	for i in range(0,len(ar)-1+s):
		for j in range(0,len(ar)-1+s):
			print(arr(i,j))
			#arr.append((i,j))


	print(arr)
	for i in arr:
		if sum(i)%k==0:
			count+=1
	print(count)
	return count






divisibleSumPairs(n, k, ar)