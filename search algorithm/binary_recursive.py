def recursive_binary_search(list, target, start=0, end=None):
    if end is None:
        end = len(list) - 1
    if start > end:
        return -1

    mid = (start + end) // 2

    if target == list[mid]:
        return mid
    else:
        if target < list[mid]:
            return recursive_binary_search(list, target, start, mid-1)
        else:
            return recursive_binary_search(list, target, mid+1, end)
        
def recursive_binary_search_v1(list,target):
    if len(list) == 0:
        return None
    else:
        midpoint = (len(list))//2
        if list[midpoint] == target:
            return True
        else:
            if list[midpoint] < target:
                return recursive_binary_search_v1(list[midpoint+1:],target)
            else:
                return recursive_binary_search_v1(list[:midpoint], target)
            
def verify(index):
    if index is not None:
        print("Target found")
    else:
        print("Target is not found in list")

if __name__ == "__main__":
    number = [1,2,3,4,5,6,7,8,9]
    number.sort()
    result = recursive_binary_search_v1(number,91)
    verify(result)

            