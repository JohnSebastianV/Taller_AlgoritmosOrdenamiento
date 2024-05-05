from Codex_AdO.Codex_Back import OrderingMethod


class RadixSort(OrderingMethod.OrderingMethod):
    @staticmethod
    def counting_sort(arr, exp): #complejidad temporal O(n), compejidad temporal O(n)
        n = len(arr) #O(1)
        output = [0] * n #O(1)
        count = [0] * 10 #O(1)

        for i in range(n):
            index = arr[i] // exp #O(1)
            count[index % 10] += 1 #O(1)

        for i in range(1, 10): #O(n)
            count[i] += count[i - 1] #O(1)

        i = n - 1 #O(1)
        while i >= 0: #O(n)
            index = arr[i] // exp #O(1)
            output[count[index % 10] - 1] = arr[i] #O(1)
            count[index % 10] -= 1 #O(1)
            i -= 1 #O(1)

        for i in range(n): #O(n)
            arr[i] = output[i] #O(1)

    @staticmethod
    def sort(arr):
        max_value = max(arr) #O(n)
        exp = 1 #O(1)
        while max_value // exp > 0: #O(n)
            RadixSort.counting_sort(arr, exp) #O(n)
            exp *= 10 #O(1)

        return arr #O(1)
