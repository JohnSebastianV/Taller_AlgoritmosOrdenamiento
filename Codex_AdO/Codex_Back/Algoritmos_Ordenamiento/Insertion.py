from Codex_AdO.Codex_Back import OrderingMethod


class InsertionSort(OrderingMethod.OrderingMethod):
    @staticmethod
    def sort(arr): #compejidad temporal 0(n), compejidad espacial O(n^2)
        for i in range(1, len(arr)):#0(n)
            key = arr[i] #0(1)
            j = i - 1 #0(1)
            while j >= 0 and key < arr[j]: #0(n)
                arr[j + 1] = arr[j]#0(1)
                j -= 1 #0(1)
            arr[j + 1] = key #0(1)
        return arr #0(1)
