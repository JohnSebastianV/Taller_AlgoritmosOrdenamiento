from Codex_AdO.Codex_Back import OrderingMethod


class BucketSort(OrderingMethod.OrderingMethod):
    @staticmethod
    def sort(arr):
        max_value = max(arr)
        min_value = min(arr)
        bucket_range = (max_value - min_value) / len(arr)

        buckets = [[] for _ in range(len(arr) + 1)]

        for num in arr:
            index = int((num - min_value) / bucket_range)
            if index == len(arr):
                index -= 1
            buckets[index].append(num)

        for i in range(len(arr)):
            buckets[i].sort()

        k = 0
        for i in range(len(arr)):
            for j in range(len(buckets[i])):
                arr[k] = buckets[i][j]
                k += 1

        return arr
