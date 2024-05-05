from Codex_AdO.Codex_Back import OrderingMethod


class QuickSort(OrderingMethod.OrderingMethod):
    @staticmethod
    def sort(arr): #compejidad temporal O(n log n), compejidad espacial O(n log n)
        if len(arr) <= 1: #O(1)
            return arr #O(1)
        pivot = arr[len(arr) // 2] #O(1)
        left = [x for x in arr if x < pivot] #O(n)
        middle = [x for x in arr if x == pivot] #O(n)
        right = [x for x in arr if x > pivot] #O(n)
        return QuickSort.sort(left) + middle + QuickSort.sort(right) #O(n log n)
