def binarySearch(array, target):
    start = 0
    end = len(array) - 1

    while start <= end:
        mid = start + (end - start) // 2  
        if array[mid] == target:
            return True
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1

    return False  

if __name__=="_main_":
    array=[1,2,3,4,5]
    target=2
    print(binarySearch(array,target))

