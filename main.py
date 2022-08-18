# Linear Search in Python
def linearSearch(array, arrayLength, numberToFind):
    # Going through array sequencially
    for i in range(0, arrayLength):
        if (array[i] == numberToFind):
            return i
    return -1

def linearSearcher(array, numberToFind):
    # Going through array sequencially
    for i in range(0, len(array)):
        if (array[i] == numberToFind):
            return i
    return -1

# def linearSearh(array, numberToFind):
#     # Going through array sequencially
#     for i in array:
#         if (array[i] == numberToFind):
#             print(i)
#             return i
#     return -1

print(linearSearcher( [2, 4, 0, 1, 9,30, 60, 70],60))
