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
    i=0
    while finaliza==False and i<3:
        
            tirada=[]
            j=0
            
            while j<5:
                valor = dado()
                tirada.append(valor) 
                j+=1           
            print(f'Tirada {tirada}')
            
            finalizar= upper_custom(input("Desea finalizar su turno?: "))
            if finalizar=="SI":
                for k in range(len(tirada)):
                    dados_guardados.append(tirada[k])
                finaliza=True
            else:
                guardar= input("Que valores de dados guarda: ")
                for l in range(len(tirada)):
                    for n in range(len(guardar)):
                        caracter=guardar[n]
                        if caracter==str(tirada[l]):
                            dados_guardados.append(tirada[l])                        
                finaliza=False
            i+=1
    print(dados_guardados)
            
            
            
            
        

def main():
    # Aqui ejecutas tus soluciones
    print(hola_mundo())
    print("Juego Generala")
    print("Turno jugador 1")
    turno()
    


# No cambiar a partir de aqui
if __name__ == "__main__":
    main()
