def naive_search(l,target):
    # l = [1,4,7,10,34]
    for i in range(len(l)):
        if l[i] == target:
            return i  
    return -1      
l = [1,5,4,7,10,34] 
l1 = [10,6,4,7,10,34]  
print(naive_search(l,10))
print(naive_search(l1,10))
 
# def binary_search(l,target):
#     # l = [1,4,7,10,34]
#     mid = len(l) // 2
#     if l[mid] == target:
#         return mid
#     elif target < l[mid]:
#         return binary_search(l,target)
#     elif target > l[mid]:
#         return binary_search(l,target)
# print(binary_search(l,10))
# print(binary_search(l1,34))
