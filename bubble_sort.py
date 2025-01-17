def bubble_sort(arr, size): #def function for bubble sort
    for i in range(0,size-1): 
        swap=False          #a variable swapping assuming that there is no swap in very start 
        for j in range(0,size-i-1):
            if arr[j]>arr[j+1]:  #checking condition if arr j is greater then j+1 .If yes!!, then they swape 
                temp=arr[j]
                arr[j]=arr[j+1]
                arr[j+1]=temp
                swap=True  # tells swapping take place 
        if not swap :#if no swapping break and return sorted array
            break
    return arr  #retrun sorted array
arr=[1,4,67,3,3,7,2,10]  #array
size=len(arr)   #length/size of the  array
result=bubble_sort(arr,size)  # calling the function 
print(result)  #printing the sorted function 
