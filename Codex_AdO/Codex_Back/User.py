class Usuario:
    @staticmethod
    def obtener_metodo_ordenamiento(metodo_elegido):
        if metodo_elegido < 1 or metodo_elegido > 9:
            print("Número de método de ordenamiento inválido. Debe estar entre 1 y 9.")
            return None
        return metodo_elegido

