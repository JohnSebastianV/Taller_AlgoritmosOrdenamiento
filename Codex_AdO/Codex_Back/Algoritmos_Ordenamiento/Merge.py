from Codex_AdO.Codex_Back import OrderingMethod
import pandas as pd


class MergeSort(OrderingMethod.OrderingMethod):

    @staticmethod
    def merge(arr1, arr2): #compejidad temporal O(n log n), compejidad espacial O(log n)
        i = 0 #O(1)
        j = 0 #O(1)
        result = [] #O(1)
        while i < len(arr1) and j < len(arr2): #O(n)
            if arr2[j] > arr1[i]: #O(1)
                result.append(arr1[i])#O(1)
                i += 1 #O(1)
            else:
                result.append(arr2[j]) #O(1)
                j += 1 #O(1)
        while i < len(arr1): #O(n)
            result.append(arr1[i]) #O(1)
            i += 1 #O(1)
        while j < len(arr2): #O(n)
            result.append(arr2[j]) #O(1)
            j += 1 #O(1)

        return result #O(1)

    @staticmethod
    def sort(arr):
        if isinstance(arr, list):
            arr = pd.Series(arr)

        if len(arr) <= 1: #O(1)
            return arr.values.tolist()

        mid = len(arr) // 2 #O(1)
        left = MergeSort.sort(arr[:mid]) #O(n log n)
        right = MergeSort.sort(arr[mid:]) #O(n log n)

        return MergeSort.merge(left, right) #O(n)
