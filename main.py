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

def ordenar_custom(lista):
    for i in range(len(lista)):
        for j in range(i + 1, len(lista)):
            if lista[i] > lista[j]:
                lista[i], lista[j] = lista[j], lista[i]
    return lista
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
    print(f'Los dados guardados son: {dados_guardados}')
    return dados_guardados

def fulls(dados_ordenados):
    if (dados_ordenados[0]==dados_ordenados[1] and dados_ordenados[0]==dados_ordenados[2] and dados_ordenados[3]==dados_ordenados[4]) or (dados_ordenados[0]==dados_ordenados[1] and dados_ordenados[2]==dados_ordenados[3] and dados_ordenados[2]==dados_ordenados[4]):
        return True
    else:
        return False        
def escaleras(dados_ordenados):
    if dados_ordenados == [1, 2, 3, 4, 5]:
        return True
    elif dados_ordenados == [2, 3, 4, 5, 6]:
        return True
    else:
        return False
def pokers(dados_ordenados):
    if (dados_ordenados[0]==dados_ordenados[1] and dados_ordenados[0]==dados_ordenados[2] and dados_ordenados[0]==dados_ordenados[3]) or (dados_ordenados[4]==dados_ordenados[3] and dados_ordenados[4]==dados_ordenados[2] and dados_ordenados[4]==dados_ordenados[1]):
        return True
    else:
        return False
def generalas(dados_ordenados):
    if dados_ordenados[0]==dados_ordenados[1] and dados_ordenados[0]==dados_ordenados[2] and dados_ordenados[0]==dados_ordenados[4] and dados_ordenados[0]==dados_ordenados[3]:
        return True
    else:
        return False
    

def opciones(dados_guardados): 
    dados_ordenados= ordenar_custom(dados_guardados) 
    escalera=escaleras(dados_ordenados)
    escalera_previa=False
    elige_escalera=False
    if escalera==True and escalera_previa==False:
        print("Puede elegir escalera 'E'")
    full = fulls(dados_ordenados)
    full_previo=False
    elige_full=False
    if full==True and full_previo==False:
        print("Puede elegir full 'F'")
    poker=pokers(dados_ordenados)
    poker_previo=False
    elige_poker=False
    if poker==True and poker_previo==False:
        print("Puede elegir poker 'P'")
    generala = generalas(dados_ordenados)
    generala_previa=False
    elige_generala=False
    if generala==True and generala_previa==False:
        print("Puede elegir generala 'G'")
        
        
           
    respuesta=upper_custom(input("Presione 'E' para escoger escalera"))
    if respuesta=="G":
        elige_generala=True
        generala_previa=True
    if respuesta=="P":
        elige_poker=True
        poker_previo=True
    if respuesta=="F":
        elige_full==True
        full_previo==True
    if respuesta=="E":
        elige_escalera==True
        escalera_previa==True
            
        
    
                  
            
            
            
        

def main():
    # Aqui ejecutas tus soluciones
    print(hola_mundo())
    print("Juego Generala")
    print("Turno jugador 1")
    dados_guardados = turno()
    


# No cambiar a partir de aqui
if __name__ == "__main__":
    main()
