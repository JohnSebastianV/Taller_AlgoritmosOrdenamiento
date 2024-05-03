from Codex_AdO.Codex_Back import OrderingMethod


class InsertionSort(OrderingMethod.OrderingMethod):
    @staticmethod
    def sort(arr):
        for i in range(1, len(arr)):
            key = arr[i]
            j = i - 1
            while j >= 0 and key < arr[j]:
                arr[j + 1] = arr[j]
                j -= 1
            arr[j + 1] = key
        return arr
