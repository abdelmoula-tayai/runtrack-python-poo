class operation:
    def __init__(self, nombre1 = 12, nombre2= 3):
        self.nombre1 = nombre1
        self.nombre2 = nombre2
    def addition(self):
        result = self.nombre1 + self.nombre2
        print("le résultat est", result)

operation_instance = operation()

operation_instance.addition()