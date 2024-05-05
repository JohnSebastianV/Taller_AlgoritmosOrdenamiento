from Codex_AdO.Codex_Back import OrderingMethod


class BubbleSort(OrderingMethod.OrderingMethod):
    @staticmethod
    def sort(arr): #compeljidad temporal O(n^2), compejidad espacial O(n)
        n = len(arr) #O(1)
        for i in range(n): #O(n)
            for j in range(0, n - i - 1):#O(n^2)
                if arr[j] > arr[j + 1]:#O(1)
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]#O(n)
        return arr #O(n)
