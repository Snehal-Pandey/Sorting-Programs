def binary(arr,l):
	flag=0
	f=0
	last=l-1
	middle=(f+last)/2
	num=input("Enter the number to search in the array: ")
	while f<last:
		
		if num>arr[middle]:
			f=middle+1
		elif num==arr[middle]:
			print "The searched number is at position ",middle+1
			flag=1
	        else:
			last=middle-1  
		if flag==1:
			break

		middle=(f+last)/2
	if f==last:	
		if num==arr[middle]:
			print "The Search number is: ",middle+1 
		else:
			print "Number not found"     
	
	




def main():
	arr=[1,5,7,9,12,15]
	length=len(arr)
	
	binary(arr,length)
	


print "Python program for binary search ==================="
main()
