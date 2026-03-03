# Tu implementacion va aqui
import random
def upper_custom(texto):
    resultado = ""
    for char in texto:
        if 'a' <= char <= 'z':
            resultado += chr(ord(char) - 32)
        else:
            resultado += char
    return resultado
def dado():
    valor=random.randint(1,6)
    return valor
def hola_mundo():
    return "hola_mundo"


def turno():
    finaliza=False
    dados_guardados=[]
    for i in range(3) and finaliza==False:
        tirada=[]
        for j in range(5-len(dados_guardados)):
            valor = dado()
            tirada.append(valor)
        finalizar= upper_custom(input("Desea finalizar su turno?: "))
        if finalizar=="SI":
            for k in range(len(tirada)):
                dados_guardados.append(tirada[k])
            
            
            
            
        

def main():
    # Aqui ejecutas tus soluciones
    print(hola_mundo())
    print("Juego Generala")
    print("Turno jugador 1")
    


# No cambiar a partir de aqui
if __name__ == "__main__":
    main()
