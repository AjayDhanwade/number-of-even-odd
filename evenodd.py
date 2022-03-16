#count the number of even odd numbers in the series of given numbers

arr=map(int,input().split())  #give the input by giving the space between two no. eg 1 2 3 4 .....
arr=list(arr)                 #converting the array input to list
print(arr)
count1=0
count2=0
for i in range(len(arr)):     #count even and odd numbers
    if (arr[i]%2==0):
        count1+=1
    else:
        count2+=1
    
print("Number of even numbers",count1)
print("number of odd numbers",count2)