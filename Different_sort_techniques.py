import random

def mergesort(arr):
    if len(arr) > 1:
        left = arr[:len(arr)//2]
        right = arr[len(arr)//2:] #The colon is important as it makes the array start from the end

        mergesort(left)
        mergesort(right)

        i = 0
        j = 0
        k = 0
        num_comparison = 0
        while i < len(left) and j < len(right):
            if left[i] < right [j]:
                arr[k] = left[i]
                i += 1
                num_comparison += 1
            else:
                arr[k] = right[j]
                j +=1    
            k +=1
            num_comparison += 1
        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            arr[k] = right[j]
            j +=1
            k +=1
        return num_comparison



def bubblesort (lt):
    n = len(lt)
    num_comparisons = 0
    for i in range (n):
        for j in range (0, n-i-1):
            num_comparisons += 1
            if lt[j] > lt[j+1]:
                lt[j], lt[j+1] = lt [j+1], lt[j]
                return num_comparisons


def selectsort(arr):
    for i in range (len(arr)):
        num_comparison = 0
        min = i
        for j in range(i+1, len(arr)):
            num_comparison +=1
            if arr[j] < arr[min]:
                min = j
        arr[i], arr[min] = arr[min], arr[i]
        return num_comparison

ranlist = [random.randint(1, 100)
        for _ in range(20)]

DList = [82, 41, 20, 58, 49, 84, 91, 48, 44, 11, 14, 56, 4, 26, 6, 50, 19, 76, 70, 78, 54, 2, 81, 5, 65, 61, 79, 32, 74, 53]
print (DList)
selectsort(DList)
num_comparison = selectsort(DList)
print (num_comparison)
print(DList)

