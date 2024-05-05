from Codex_AdO.Codex_Back.Algoritmos_Ordenamiento import Bubble, Bucket, Counting, Heap, Insertion, \
    Merge, Quick, Radix, Selection


class Creator:
    def __init__(self):
        self.dict_classes = {
            1: Radix.RadixSort(),
            2: Merge.MergeSort(),
            3: Bucket.BucketSort(),
            4: Heap.HeapSort(),
            5: Insertion.InsertionSort(),
            6: Quick.QuickSort(),
            7: Bubble.BubbleSort(),
            8: Selection.SelectionSort(),
            9: Counting.CountingSort()
        }

    def method_order(self, num, arr, column): # compeljidad temporal O(n^2), complejidad espacial O(n^2)
        dictionarynames = {
            1: "RadixSort",
            2: "MergeSort",
            3: "BucketSort",
            4: "HeapSort",
            5: "InsertionSort",
            6: "QuickSort",
            7: "BubbleSort",
            8: "SelectionSort",
            9: "CountingSort"
        }
        classes = self.dict_classes.get(num)
        if classes:
            orderedarrangement = classes.sort(arr)
            methodname = dictionarynames.get(num)
            message = f"El array fue ordenado utilizando el método de ordenamiento {methodname} y la columna {column}."
            return orderedarrangement, message
        else:
            print("Número de método de ordenamiento no válido")
