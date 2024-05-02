from Codex_AdO.Codex_Back.Algoritmos_Ordenamiento import Bubble,  Bucket, Counting, Heap, Insertion, Merge, Quick, Radix, Selection


class Creator:
    def __init__(self):
        self.dict_clases = {
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

    def ordenar(self, num, arr, columna):
        metodo_nombres = {
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
        clase = self.dict_clases.get(num)
        if clase:
            array_ordenado = clase.sort(arr)
            nombre_metodo = metodo_nombres.get(num)
            mensaje = f"El array fue ordenado utilizando el método de ordenamiento {nombre_metodo} y la columna {columna}."
            return array_ordenado, mensaje
        else:
            print("Número de método de ordenamiento no válido")


