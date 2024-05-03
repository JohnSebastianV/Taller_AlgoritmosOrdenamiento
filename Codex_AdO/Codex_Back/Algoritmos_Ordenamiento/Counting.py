from Codex_AdO.Codex_Back import OrderingMethod


class CountingSort(OrderingMethod.OrderingMethod):
    @staticmethod
    def sort(arr):
        max_value = max(arr)
        min_value = min(arr)
        count = [0] * (max_value - min_value + 1)

        for num in arr:
            count[num - min_value] += 1

        sorted_arr = []
        for i in range(len(count)):
            sorted_arr.extend([i + min_value] * count[i])

        return sorted_arr
