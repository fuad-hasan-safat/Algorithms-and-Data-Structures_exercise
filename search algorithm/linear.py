def linear_search(lst, target):
    """
    Return index position of target if found, else return None
    """
    for index, value in enumerate(lst):
        if value == target:
            return index
    return None

def verify(index):
    if index is not None:
        print("Target found at index: ",index)
    else:
        print("Target is not found in list")

if __name__ == "__main__":
    number = [1,2,3,4,5,6,9,8,7]
    result = linear_search(number,9)
    verify(result)