# ITERATIVE METHOD :-
def binarysearch(start, end, data):
    while end >= start:
        mid = start + (end - start) // 2
        if arr[mid] == data:
            return mid
        elif arr[mid] > data:
            end = mid - 1
        else:
            start = mid + 1




# arr = [1,2,3,4,5,6,7,8,9]
# data = 7
# bin = binarysearch(0, len(arr)-1, data)
# print(bin)
