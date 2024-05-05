from Codex_AdO.Codex_Back import OrderingMethod


class SelectionSort(OrderingMethod.OrderingMethod):
    @staticmethod
    def sort(arr): #compejidad temporal #O(n^2), compejdad espacial #O(1)
        n = len(arr) #O(1)
        for i in range(n): #O(n)
            min_idx = i #O(1)
            for j in range(i + 1, n):#O(n)
                if arr[j] < arr[min_idx]: #O(1)
                    min_idx = j #O(1)
            arr[i], arr[min_idx] = arr[min_idx], arr[i]#O(1)
        return arr#O(1)
