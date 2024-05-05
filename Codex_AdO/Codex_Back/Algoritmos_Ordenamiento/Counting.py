from Codex_AdO.Codex_Back import OrderingMethod


class CountingSort(OrderingMethod.OrderingMethod):
    @staticmethod
    def sort(arr):# compejidad temporal O(n), compejidad espacial O(n + m)
        max_value = max(arr)#O(n)
        min_value = min(arr)#O(n)
        count = [0] * (max_value - min_value + 1)#O(1)

        for num in arr:#O(n)
            count[num - min_value] += 1#O(1)

        sorted_arr = []#O(1)
        for i in range(len(count)):#O(n)
            sorted_arr.extend([i + min_value] * count[i])#O(1)

        return sorted_arr#O(1)
