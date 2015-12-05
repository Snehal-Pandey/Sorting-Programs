def bubblesort(arr,l):
	for k in range(l-1):
		for i in range(l-1):
			for j in range(i+1,l):
				if arr[j]<arr[i]:
					temp=arr[j]
					arr[j]=arr[i]
					arr[i]=temp
				break
	return arr





def main():
	arr=[5,7,1,15,12,9]
	length=len(arr)
	res=bubblesort(arr,length)
	print "The sorted array of bubble sort is:"
	for s in res:	
		print s," "

main()
	
