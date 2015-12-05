import os
def quicksort(arr,l):
	for i in range(l-1):
		for j in range(i+1,l):
			if arr[i]>arr[j]:
				temp=arr[j]
				arr[j]=arr[i]
				arr[i]=temp
	
	return arr




def main():
	os.system('clear')
	arr=[5,7,1,15,12,9]
	length=len(arr)
	print "Array after Sorting is:"
	res=quicksort(arr,length)
	for s in res:
		print s," "
	
	linearsearch(res)
	
def linearsearch(res):
	flag=0
	no=input("Enter the number you want to search: ")
	for i in range(len(res)):
		if no==res[i]:
			pos=i+1
			flag=1
			break;

	if flag==0:
		print " The number is not available in the array"
	else:
		print "The Searched number is at position ",pos,"\nThe searched number is:",no





print "Python program for Linear Search is ==================="
main()
