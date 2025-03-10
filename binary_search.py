def binary_search(arr, target):
    left = 0
    right = len(arr)-1

    while left<right:
        mid = (left+ right)//2
        print(mid)

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left  = mid+1
        elif arr[mid] > target:
            right  = mid-1
    
    return -1


array = [1,3,5,7,9,11] #5
target = 3
result = binary_search(array,target)

if result != -1:
    print(f"Target {target} found at index {result}.")
else:
    print(f"Target {target} not found in the array.")