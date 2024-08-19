class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    
    def saludar(self):
        return f'Hola, me llamo {self.nombre} y tengo {self.edad} años.'
    
def main():
    persona1 = Persona('Juan', 34)
    print(persona1.saludar())

if __name__ == "__main__":
    main()
