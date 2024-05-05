from Codex_AdO.Codex_Back import OrderingMethod


class HeapSort(OrderingMethod.OrderingMethod):
    @staticmethod
    def heapify(arr, n, i):# compejidad temporal O(n log n), complejidad espacial O(1)
        largest = i #O(1)
        left = 2 * i + 1 #O(1)
        right = 2 * i + 2 #O(1)

        if left < n and arr[left] > arr[largest]: #O(1)
            largest = left #O(1)

        if right < n and arr[right] > arr[largest]:#O(1)
            largest = right #O(1)

        if largest != i: #O(1)
            arr[i], arr[largest] = arr[largest], arr[i] #O(1)
            HeapSort.heapify(arr, n, largest)#O(n log n)

    @staticmethod
    def sort(arr):
        n = len(arr) #O(1)

        for i in range(n // 2 - 1, -1, -1): #O(n)
            HeapSort.heapify(arr, n, i)#O(n log n)

        for i in range(n - 1, 0, -1): #O(n)
            arr[i], arr[0] = arr[0], arr[i] #O(1)
            HeapSort.heapify(arr, i, 0)#O(log i)

        return arr #O(1)
