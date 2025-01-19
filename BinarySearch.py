def binary_search(arr, t):
    l = 0
    r = len(arr)-1

    while l <= r:
        mid = (l+r)//2
        if arr[mid] == t:
            return mid
        elif arr[mid]<t:
            l = mid+1
        else:
            r = mid-1

    return -1

n = [11,29,36,55,60,67,77,99]
t = 77

r = binary_search(n, t)
if r != -1:
    print(f"Target {t} is at index {r}.")
else:
    print("Target not found.")