# RECURSIVE METHOD :-
def binarysearch(start, end, data):
    if end >= start:
        mid = start + (end - start) // 2
        if arr[mid] == data:
            return mid
        elif arr[mid] > data:
            return binarysearch(start, mid-1, data)
        else:
            return binarysearch(mid+1, end, data)
          
          
          
# arr = [1,2,3,4,5,6,7,8,9]
# data = 7
# bin = binarysearch(0, len(arr)-1, data)
# print(bin)    
