#import os

def insertionsort(arr,l):
	for i in range(1,l):
		j=i
		while j>0 and arr[j]<arr[j-1]:
			temp=arr[j]
			arr[j]=arr[j-1]
			arr[j-1]=temp
			j-=1
	return arr

def main():
	arr=[12,34,1,78,56,33]
	length=len(arr)
	res=insertionsort(arr,length)		
	print "The sorted array is:==============="
	for s in res:
		print s


print ("\nWelcome to the world of Insertion sort...................\n").upper()
main()
