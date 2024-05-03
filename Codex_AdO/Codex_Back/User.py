class User:
    @staticmethod
    def get_sort_method(method):
        if method < 1 or method > 9:
            print("Número de método de ordenamiento inválido. Debe estar entre 1 y 9.")
            return None
        return method
