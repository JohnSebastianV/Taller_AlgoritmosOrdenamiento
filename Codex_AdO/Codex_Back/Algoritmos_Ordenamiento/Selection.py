from Codex_AdO.Codex_Back import OrderingMethod


class SelectionSort(OrderingMethod.OrderingMethod):
    @staticmethod
    def sort(arr):
        n = len(arr)
        for i in range(n):
            min_idx = i
            for j in range(i + 1, n):
                if arr[j] < arr[min_idx]:
                    min_idx = j
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
        return arr
