with open("QuickSort.txt", "r") as f:
    arr = list(map(int, f.readlines()))


def partition(arr, l, r, pivotvalidx):
    # swap pivot value to first value
    
    arr[l], arr[pivotvalidx] = arr[pivotvalidx], arr[l]
    i = l+1
    pivotval = arr[l]
    for j in range(l+1, r+1):
        if arr[j] < pivotval:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
    arr[l], arr[i-1] = arr[i-1], arr[l]
    return i-1

def choosepivot(arr, start, end, meth=0):
    if meth==0:
        return start
    elif meth == 1:
        return end
    elif meth == 2:
        first = arr[start]
        last = arr[end]
        midindex= (start+end)//2
        middle = arr[midindex]

        # if first < middle and middle < last:
        #     return midindex
        # elif middle < first and first < last:
        #     return start
        # else:
        #     return end

        meds = [first, middle, last]
        meds.sort()
        if meds[1] == first:
            return start
        if meds[1] == last:
            return end
        if meds[1] == middle:
            return midindex
    
compcount = 0
def quicksort(arr, start, end):
    global compcount
    if start >= end:
        return
    compcount += (end-start)
    # question 1 - method zero
    # pivotvalidx = choosepivot(arr, start, end)
    # pivotvalidx = choosepivot(arr, start, end, 1)
    pivotvalidx = choosepivot(arr, start, end, 2)
    p = partition(arr, start, end, pivotvalidx)
    quicksort(arr, start, p-1)
    quicksort(arr, p+1, end)

# arr = [4,5,7,1,2]
quicksort(arr, 0, len(arr) - 1)
# print(arr)
print(compcount)