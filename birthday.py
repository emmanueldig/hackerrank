s3=[1,2,1,3,2]
d3=3
m3=2
s1=[1,1,1,1,1,1]
d1=3
m1=2
s2=[4]
d2=4
m2=1
s4=[0,1,2,3,4,5,6,7,8,9]
d4=4
m4=4


def birthday(s,d,m):
	count=0
	arr=[s[i:i+m] for i in range(0, len(s)+1-m)]
	for i in arr:
		if d==sum(i):
			count+=1
	print(count)



birthday(s4,d4,m4)
#birthday(s2,d2,m2)
#birthday(s3,d3,m3)
#birthday(s1,d1,m1)