print("Clases V2 saul jimenez")
# zona de clase
class Datos:
    # el constructor funcion
    def __init__(self,estatura,peso):
        self.estatura=estatura
        self.peso=peso
    def mostrar_datos(self):
        print(f"Estatura : {self.estatura}mts, Peso {self.peso} Kg")
    def mi_lista(self):
        cantante=["badbyny", "nata", "cr7"]
        print(cantante)
        for miu in cantante:
            print(miu)
    def mi_tupla(self):
        tupla_razas=("Doberman","Labrador","Pastor Aleman")
        for b in tupla_razas:
            print(b)

    def mi_conjunto(self):
        conjunto_carros={"ferrari","buggatti","mercedez","bocho"}
        for c in conjunto_carros:
            print(c)

    def mi_dic(self):
        dic_edadP={"elio":"17","vencia":"7","fany":"27"}
        for d,e in dic_edadP.items():
            print(d,e)

# creacion de objeto
info=Datos(1.75,70.5)


# utilizando el obj.--> info
info.mostrar_datos()
print(" Lista de nombres de Cantantes de saul jimenez")
info.mi_lista()
print("\nTupla razas de perros de saul jimenez")
info.mi_tupla()
print("\nConjunto de carros de saul ")
info.mi_conjunto()
print("\nDiccionario edades")
info.mi_dic()

# utilizando el objeto
info.mostrar_datos()

