def mergeSort(myList):
    if len(myList) > 1:
        mid = len(myList) // 2
        left = myList[:mid]
        right = myList[mid:]

        print("mid :", mid)
        print("left :", left)
        print("right :", right)

        #  recursive call on each half
        mergeSort(left)
        mergeSort(right)

        # Two iterators for traversing the two halves
        i = 0
        j = 0

        #iterators for the main list
        k = 0


        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                # The value from the left half has been used
                myList[k] = left[i]
                print("Current result :", myList)
                i += 1
            else :
                myList[k] = right[j]
                print("Current result : ",myList)
                j += 1
            # move to the next slot
            k += 1

        # for all remaining values
        while i < len(left):
            myList[k] = left[i]
            print("Current result : ",myList)
            i += 1
            k += 1

        while j < len(right):
            myList[k] = right[j]
            print("Current result : ",myList)
            j += 1
            k += 1 

myList =[54,36,93,17,77,31,44,55,20]
print(myList)
mergeSort(myList)
print(myList)


