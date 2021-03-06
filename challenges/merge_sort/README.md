## Challenge

Trace the algorithm by stepping through the process with the provided sample array. Document your explanation by creating a blog article that shows the step-by-step output after each iteration through some sort of visual.

## Approach & Efficiency

time <- O(n)
space <- O(n)

## White Board

![image](https://user-images.githubusercontent.com/79086986/125357608-81e45800-e370-11eb-976d-9514371ff542.png)


## Code

```
def merge_sort(arr):
    n = len(arr)

    if n > 1:

        mid = n//2
        left = arr[:mid]
        right = arr[mid:]

        merge_sort(left)
        merge_sort(right)

        merge_left_and_right(left, right, arr)

    print(arr)
    return arr

def merge_left_and_right(left, right, arr):
    i, j, k = 0, 0, 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1

        k += 1

    while i < len(left):
        arr[k] = left[i]
        i += 1
        k += 1

    while j < len(right):
        arr[k] = right[j]
        j += 1
        k += 1


arr = [8,4,23,42,16,15]
merge_sort(arr)
```
