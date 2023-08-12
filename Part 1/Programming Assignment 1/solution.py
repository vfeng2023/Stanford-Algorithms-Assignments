def countinversions(arr):
    # count left inversions, 
    # count right inversions
    # merge
    buffer = [0 for i in range(len(arr))]
    def splitinv(begin, mid, end):
        # if begin >= mid:
        #     return 0
        nonlocal buffer, arr
        i = begin
        j = mid+1
        total = 0
        idx = begin
        while i <= mid and j <= end:
            if arr[i] < arr[j]:
                buffer[idx] = arr[i]
                idx += 1
                i += 1
            else:
                buffer[idx] = arr[j]
                total += mid - i + 1
                idx += 1
                j += 1
        while i <= mid:
            buffer[idx] = arr[i]
            i += 1
            idx += 1
        while j <= end:
            buffer[idx] = arr[j]
            idx += 1
            j += 1
        for k in range(begin, end + 1):
            arr[k] = buffer[k]
        return total
    def count(start, end):
        if start >= end:
            return 0
        nonlocal buffer, arr
        mid = (start + end) // 2
        left = count(start, mid)
        right = count(mid+1, end)
        split = splitinv(start, mid, end)
        return left + right + split
    
    return count(0, len(arr) - 1)


# read file
with open("I:\\My Drive\\UVA CS stuff\\Stanford-Algorithms-Assignments\\Programming Assignment 1\\IntegerArray.txt") as f:
    lines = f.readlines()
    intarr = list(map(int, lines))
# intarr = [5,6,7,1,2,3,4]
# intarr = [1,2,3,4,5,6,7]
result = countinversions(intarr)

# print(intarr)
print(result)

