def linear_search(arr, t):
    for i, v in enumerate(arr):
        if v==t:
            return i
    return -1

n = [22,35,19,18,26,37,49]
t = 39

r = linear_search(n, t)
if r != -1:
    print(f"Target {t} is at index {r}.")
else:
    print("Target not found.")