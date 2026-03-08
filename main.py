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
    intentos=0
    while finaliza==False and intentos<3:
        tirada=[]
        for j in range(5-len(dados_guardados)):
            valor = dado()
            tirada.append(valor) 
        print(f'Tirada {intentos+1}: {tirada}')
            
        if intentos<2:
            finalizar= upper_custom(input("Desea finalizar su turno?: "))
            if finalizar=="SI":
                for k in range(len(tirada)):
                    dados_guardados.append(tirada[k])
                finaliza=True
            else:
                guardar= input("Que valores de dados guarda: ")
                for l in range(len(tirada)):
                    if str(tirada[l]) in guardar:
                        dados_guardados.append(tirada[l]) 
        else:
            for z in range(len(tirada)):
                dados_guardados.append(tirada[z])
            finaliza=True
        intentos+=1
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
