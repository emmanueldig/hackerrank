d1=[1, 4, 4, 4, 5, 3]
d1=[1, 2, 3, 4, 5, 4, 3, 2, 1, 3, 4]
d1=[0, 5, 3, 5, 2, 4, 0, 3, 4, 5, 0, 1, 5, 0, 5, 5, 1, 5, 3, 3, 2, 1, 5, 5, 4, 1, 2, 3, 1, 5, 5, 3, 3, 2, 4, 3, 2, 5, 4, 3, 1, 4, 5, 2, 2, 3, 0, 1, 2, 0, 4, 1, 3, 3, 0, 2, 5, 3, 4, 0, 3, 0, 1, 1, 0, 5, 2, 0, 5, 3, 0, 1, 5, 5, 2, 5, 4, 0, 2, 5, 3, 4, 2, 4, 2, 0, 5, 5, 4, 1, 5, 0, 4, 5, 1, 0, 4, 0, 4, 1]
d1=[1, 4, 4, 4, 5, 3]
d=[3, 1, 1, 2, 4, 1, 1, 2, 1, 4, 1, 2, 4, 2, 2, 2, 5, 1, 3, 1, 2, 2, 1, 1, 2, 4, 2, 2, 2, 2, 1, 1, 2, 5, 2, 1, 1, 1, 2, 1, 2, 1, 3, 1, 1, 2, 1, 5, 1, 4, 1, 1, 1, 3, 5, 2, 1, 1, 4, 2, 4, 2, 2, 2, 1, 1, 3, 2, 2, 1, 3, 5, 4, 2, 2, 4, 4, 5, 2, 2, 2, 3, 1, 2 ,1 ,2 ,3 ,2 ,2 ,1 ,1 ,2 ,5 ,2 ,2 ,1 ,1 ,1 ,2 ,1 ,1 ,1 ,1 ,2, 1, 2, 1, 2, 2, 5, 1, 4, 1, 2, 2, 2, 2, 1, 1, 2, 2, 2, 3 ,2 ,2, 2, 2, 2, 2, 2, 3, 1, 1, 5, 2, 1, 2, 1, 2, 4, 2, 2, 1, 2, 1, 2, 1, 2, 2, 1, 2, 1, 2, 4, 2, 5, 2, 4, 4, 2, 4, 1, 1, 2, 2, 2, 2, 4, 1, 5, 2, 2, 1, 1, 1, 2, 1, 1, 2, 2, 1, 4, 1, 2, 1, 4, 1, 4, 2, 1, 4, 2, 1, 1, 1, 4, 3, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 4, 1, 2, 2, 1, 2, 1, 4, 3, 4, 2, 4, 1, 2, 1, 3, 2, 2, 5, 2, 1, 1, 1, 2, 2, 1, 4, 1, 1, 2, 1, 5, 4, 2, 1, 2, 1, 1, 2, 1, 2, 2, 1, 5, 2, 4, 1, 2, 2, 1, 2, 2, 1, 2, 1, 2, 2, 3, 2, 1, 2, 1, 2, 1, 1, 4, 1, 2, 2, 4, 2, 2, 1, 1, 1, 1, 2, 4, 1, 2, 1, 3, 1 ,2 ,2 ,1 ,2 ,5 ,1 ,1, 2, 2, 2, 1, 1, 1 ,1 ,1 ,4 ,2 ,1 ,2 ,2 ,1 ,2 ,1 ,4 ,1 ,2 ,2 ,1 ,2 ,2 ,2 ,2 ,2 ,2 ,4 ,2 ,1 ,5 ,1 ,2 ,3 ,2 ,4 ,2 ,1 ,1 ,2 ,1 ,1 ,2, 1, 3, 1, 2, 2, 2, 2, 2, 4, 3, 1, 2, 1, 3, 2, 4, 2, 4, 4, 1, 2, 5, 3, 1, 4, 1, 2, 2, 1, 2, 2, 4, 1, 2, 3 ,1 ,1 ,1 ,3 ,1 ,5 ,1, 2, 2, 1, 2, 2, 1, 1, 1, 1, 1, 4, 2, 3, 3, 2 ,2 ,1 ,2 ,1 ,2 ,1 ,1 ,4 ,5 ,2 ,2 ,2 ,2 ,2, 1, 2, 1, 1, 5, 2, 4, 1, 1, 1, 1, 2, 2, 2, 2, 3, 2, 2, 1, 5, 5, 2, 5, 2, 2, 2, 1, 1, 2, 1, 4, 2, 4, 2 ,1 ,1 ,2 ,2 ,1 ,4 ,2 ,4 ,2 ,1 ,2 ,1 ,1 ,1 ,2 ,4 ,2, 2, 3, 1, 1, 2, 2, 1, 2, 2, 1, 1, 2, 2, 1, 1, 1, 2, 4, 1, 1, 1, 1, 1, 5, 2, 1, 5, 1, 2, 4, 2, 2, 1, 2, 1, 1, 4, 1, 2, 1, 1, 1, 1, 2, 1, 1, 1]
from random import randrange 
def bird2():
	c=[]
	for i in range(100):
		c.append(randrange(0,6))
	print(c)
	return c 

arr=[]
def bird1(a):
	count1=0
	count2=0
	count3=0
	count4=0
	count5=0
	for i in a:
		if i==1:
			count1+=1
		elif i==2:
			count2+=1
		elif i==3:
			count3+=1
		elif i==4:
			count4+=1
		elif i==5:
			count5+=1
	arr=[count1,count2,count3,count4,count5]
	arr1=[25,25,56,56,25]
	print(arr)
	index=[]
	max1=max(arr)  # "max" function to find largest number in the list
	"""for i in range(0,len(arr)):
		for j in range(i+1,len(arr)):
			if arr[i]<arr[j] and arr[i]>arr[j]:
				max=arr[j]
			if arr[i]>arr[j]:"""

	for i in range(0,len(arr)):   # loop through the list to find if similer max1 number exits?
			if max1==arr[i]:
				index.append(i)

	print(max1)
	print(index)
	print(index[0]+1)
	#print(index[0]+1)







	
	"""for index,number in enumerate(arr):
		for i in range(0,len(arr)):
			for j in range(i+1,len(arr)):
				print(index, number,i,j)"""
	"""index=[]
	for i in range(0,len(arr)):
		for j in range(i+1,len(arr)):
			if arr[i]==arr[j]:
				samp=[arr[i],i]
				samp1=[arr[j],j]
				index.append(samp)
				index.append(samp1)
	print(index)
	maxnumber=0

	index1= index.copy()
	for x in range(0,len(index1)):
		for y in range(x+1,len(index1)):
			if index1[x][-1]==index1[y][-1]:
				index.remove(index1[y])
	print(index)
	for x1 in range(0,len(index)):
		for y1 in range(x1+1,len(index)):
			if index[x1][0]<index[y1][0]:
				maxnumber=index[y1][0]
				print(maxnumber)
				break
			if index[x1][0]==index[y1][0]:
				maxnumber=index[y1][0]
				print(maxnumber)
				break
	#initval=0
	#smallest=0

	for x11 in range(0,len(index)):
		if index[x11][0]==maxnumber:
			initval=index[x11][1]
			break
	print(initval+1)"""


	#print(initval)
	#print(smallest)
			#abc.append(x)
	#print(abc)





	"""maxarray=[]
	maxvalue=0
	equalvalue=0
	maxvaluearray=[]
	for index,number in enumerate(arr):
		if maxvalue < number or (maxvalue==number and number != 0):
		
			maxvalue=number
			maxarray.append(index)
			maxvaluearray.append(number)
			#print(maxvalue)
			print(maxarray)
			print(maxvaluearray)
	store=maxvaluearray[0]
	for x in maxvaluearray:
		store=x
		if x==store:

			print(x) """

		#print(index,number)				#working
		#if number>number[index+1]
		#print(index,arr[index:index+1])	#working
		#print(index,arr[index])
	"""count=0
	for j in arr:			#this whole for loop is working
		last=len(arr)
		print(j,arr.index(j,count,last))
		count+=1"""


		#count[i]
	#print(count)
#rand=bird2()



"""max=arr[0]
	for i in range(0,len(arr)):
		if arr[i] > max:
			max = arr[i] 
	print(max)
	x=[]
	for i in range(0,len(arr)):
		if arr[i]==max:
			x.append(i)
	print(x)
	for i in range(0,len(x)):
		if x[i]
	#largest=arrsorted[-1]
	#print(largest)"""
	
	"""print(arr1)
	x=[]

	for i in range(1,len(arr)):
		for j in range(i+1,len(arr)):
			if (arr[i]==arr[j] and  ):
				y=i
				z=j
				x.append(y)
				x.append(j)
	#x=list(x[0])
	print(x)"""
	"""for i in range(0,len(x)):
		for j in range(i+1,len(x)):
			if (x[i]==x[j]):
				print("xi",x[i],"xj",x[j])
				print(x.remove(x[j]))
				print(x)"""



	#index=[]
	
	"""for index,number in enumerate(arr):
		for i in range(0,len(arr)):
			for j in range(i+1,len(arr)):
				print(index, number,i,j)


	#abc=[]
	#abc=[arr[i:i+2] for i in range(0,len(arr)-1)]  """
	"""for i in range(0,len(arr)):
		for j in range(i+1,len(arr)):
			if arr[i]==arr[j]:
				samp=(i,j)
				index.append(samp)
	print(index)"""
			#abc.append(x)
	#print(abc)





	"""maxarray=[]
	maxvalue=0
	equalvalue=0
	maxvaluearray=[]
	for index,number in enumerate(arr):
		if maxvalue < number or (maxvalue==number and number != 0):
		
			maxvalue=number
			maxarray.append(index)
			maxvaluearray.append(number)
			#print(maxvalue)
			print(maxarray)
			print(maxvaluearray)
	store=maxvaluearray[0]
	for x in maxvaluearray:
		store=x
		if x==store:

			print(x) """

		#print(index,number)				#working
		#if number>number[index+1]
		#print(index,arr[index:index+1])	#working
		#print(index,arr[index])
	"""count=0
	for j in arr:			#this whole for loop is working
		last=len(arr)
		print(j,arr.index(j,count,last))
		count+=1"""


		#count[i]
	#print(count)
#rand=bird2()


bird1(d)



