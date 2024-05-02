from Codex_AdO.Codex_Back import MetodoOrdenamiento


class QuickSort(MetodoOrdenamiento.MetodoOrdenamiento):
    @staticmethod
    def sort(arr):
        if len(arr) <= 1:
            return arr
        pivot = arr[len(arr) // 2]
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        return QuickSort.sort(left) + middle + QuickSort.sort(right)
