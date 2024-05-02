from Codex_AdO.Codex_Back.Algoritmos_Ordenamiento import Bubble,  Bucket, Counting, Heap, Insertion, Merge, Quick, Radix, Selection


class Creator:
    def __init__(self):
        self.dict_clases = {
            1: Bubble.BubbleSort(),
            2: Bucket.BucketSort(),
            3: Counting.CountingSort(),
            4: Heap.HeapSort(),
            5: Insertion.InsertionSort(),
            6: Merge.MergeSort(),
            7: Quick.QuickSort(),
            8: Radix.RadixSort(),
            9: Selection.SelectionSort()
        }

    def ordenar(self, num, arr, columna):
        metodo_nombres = {
            1: "BubbleSort",
            2: "BucketSort",
            3: "CountingSort",
            4: "HeapSort",
            5: "InsertionSort",
            6: "MergeSort",
            7: "QuickSort",
            8: "RadixSort",
            9: "SelectionSort"
        }
        clase = self.dict_clases.get(num)
        if clase:
            array_ordenado = clase.sort(arr)
            nombre_metodo = metodo_nombres.get(num)
            mensaje = f"El array fue ordenado utilizando el método de ordenamiento {nombre_metodo} y la columna {columna}."
            return array_ordenado, mensaje
        else:
            print("Número de método de ordenamiento no válido")


