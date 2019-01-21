A = [2,1,0]




def mergeSort(array, counter = 0):
    print("Splitting ",array)
    if len(array) == 1:
        return(array, counter)
    else:
        mid = len(array)//2
        left = array[:mid]
        right = array[mid:]
        counter +=3
        
        print('left',left)
        print('counter',counter)
        left, counter = mergeSort(left,counter)
        right, counter = mergeSort(right,counter)
        
        i = 0
        j = 0
        k = 0
            
        while i < len(left) and j < len(right):
            counter+=1
            if left[i] < right[j]:
                array[k] = left[i]
                i+=1
            else:
                array[k] = right[j]
                j+=1
            k+=1
        
        
        while i < len(left):
            counter+=1
            array[k]=left[i]
            i+=1
            k+=1

        while j < len(right):
            counter+=1
            array[k]=right[j]
            j+=1
            k+=1
        
        print(array,counter)
        return(array,counter)

    
mergeSort(A)
print(A)