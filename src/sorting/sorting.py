# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements
    x = 0

    # Your code here
    for i in range(0, len(merged_arr)):
        if len(arrA) + len(arrB) == 0:
            return
        if len(arrA) + len(arrB) == 1:
            if len(arrA) != 0:
                merged_arr[i] = arrA[0]
                arrA.pop(0)
            else:
                merged_arr[i] = arrB[0]
                arrB.pop(0)
        elif len(arrA) == 0 and len(arrB) != 0:
            if arrB[0] < arrB[1]:
               merged_arr[i] = arrB[0]
               arrB.pop(0)
            else:
                merged_arr[i] = arrB[1]
                arrB.pop(1)
        elif len(arrB) == 0 and len(arrA) != 0:
            if arrA[0] < arrA[1]:
               merged_arr[i] = arrA[0]
               arrA.pop(0)
            else:
                merged_arr[i] = arrB[1]
                arrB.pop(1)
        elif arrA[0] < arrB[0]:
            merged_arr[i] = arrA[0]
            arrA.pop(0)
        else:
            merged_arr[i] = arrB[0]
            arrB.pop(0)
    return merged_arr

# TO-DO: implement the Merge Sort function below recursively
def merge_sort(arr):
#     # Your code here
    if len(arr) <= 1:
        return arr
    else:
        middle = len(arr) // 2
        left = merge_sort(arr[:middle])
        right = merge_sort(arr[middle:])
        
    return merge(left, right)

# arr = [1, 5, 8, 4, 2, 9, 6, 0, 3, 7]
# print(arr[:5])
# print(arr[5:])

# STRETCH: implement the recursive logic for merge sort in a way that doesn't 
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists 
# or data structures; it can only re-use the memory it was given as input
# def merge_in_place(arr, start, mid, end):
#     # Your code here


# def merge_sort_in_place(arr, l, r):
    # Your code here

