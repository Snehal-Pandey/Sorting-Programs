def selection_sort(arr,l):
	for i in range(l-1):
		min_position=i
		for j in range(i+1,l):
			if arr[j]<arr[min_position]:
				min_position=j
		
		if(min_position!=i):
			temp=arr[i]
			arr[i]=arr[min_position]
			arr[min_position]=temp

	return arr

def main():
	arr=[20,12,45,23,55,11]
	length=len(arr)
	res=selection_sort(arr,length)	
	print "The Sorted array is:"
	for s in res:
		print s,"\n"

print "Program for selection sort................."
main()
