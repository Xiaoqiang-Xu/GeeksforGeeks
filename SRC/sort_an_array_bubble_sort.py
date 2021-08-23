class Solution:
    #Function to sort the array using bubble sort algorithm.
    def bubbleSort(self,arr, n):
        # code here
        for i in range(0, n):
            swapped = False
            for j in range(0, n - i - 1):
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
                    swapped = True
            if swapped == False:
                break
        return arr
