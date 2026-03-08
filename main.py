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
    bonus=0
    while finaliza==False and intentos<3:
        tirada=[]
        for j in range(5-len(dados_guardados)):
            valor = dado()
            tirada.append(valor) 
        print(f'Tirada {intentos+1}: {tirada}')
        
        if intentos==0:
            tirada_ord=ordenar_custom(tirada)
            bonusE= escaleras(tirada_ord)
            bonusF= fulls(tirada_ord)
            bonusP= pokers(tirada_ord)
            generala_real= generalas(tirada_ord)
            if bonusE==True or bonusF==True or bonusP==True:
                print("Gana bonus")
                bonus+=5
            if generala_real==True:
                bonus+=30
                print("Generala real")
            
            
            
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
    dados_ord= ordenar_custom(dados_guardados)
    return dados_ord,bonus,generala_real

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
def opciones(dados_guardados, categorias_usadas, numeros_usados): 
    dados_ordenados = ordenar_custom(dados_guardados) 
    
    escalera = escaleras(dados_ordenados)
    if escalera == True:
        print("Puede elegir escalera 'E'")
        
    full = fulls(dados_ordenados)
    if full == True:
        print("Puede elegir full 'F'")
        
    poker = pokers(dados_ordenados)
    if poker == True:
        print("Puede elegir poker 'P'")
        
    generala = generalas(dados_ordenados)
    if generala == True:
        print("Puede elegir generala 'G'")
        
    print("Puede elegir numeros 'N'")       
    
    puntaje = 0
    categoria_valida = False
    
    while categoria_valida == False: 
        respuesta = upper_custom(input("Presione la letra correspondiente a la categoria que desea elegir: "))
        
        if respuesta == "N":
            dado_elegido = int(input("Ingrese el dado que elige: "))
            if dado_elegido not in numeros_usados: 
                numeros_usados.append(dado_elegido)
                apariciones = 0
                for j in range(len(dados_ordenados)):
                    if dados_ordenados[j] == dado_elegido:
                        apariciones += 1
                suma = dado_elegido * apariciones
                puntaje += suma
                categoria_valida = True 
            else:
                print("Ya eligio ese numero anteriormente. Elija otro.") 
                
        elif respuesta == "G" or respuesta == "P" or respuesta == "F" or respuesta == "E": 
            if respuesta not in categorias_usadas: 
                categorias_usadas.append(respuesta) 
                if respuesta == "G":
                    puntaje += 50
                if respuesta == "P":
                    puntaje += 40
                if respuesta == "F":
                    puntaje += 30
                if respuesta == "E":
                    puntaje += 20
                categoria_valida = True 
            else:
                print("Ya utilizo esta categoria en un turno anterior. Elija otra.") 
        else:
            print("Letra incorrecta. Por favor ingrese N, G, P, F o E.")

    return puntaje     
def main():
    # Aqui ejecutas tus soluciones
    print(hola_mundo())
    print("Juego Generala")
    categorias_j1 = [] 
    numeros_j1 = []
    puntaje_tot1=0
    categorias_j2 = []
    numeros_j2 = []
    puntaje_tot2 = 0
    generala_real1=False
    generala_real2=False
    while generala_real1==False and generala_real2==False and len(categorias_j1)+len(numeros_j1)<11 and len(categorias_j2)+len(numeros_j2)<11:
        print("Turno jugador 1")
        dados_guardados, bonus, generala_real1 = turno()
        puntaje_parcial = opciones(dados_guardados, categorias_j1, numeros_j1) 
        puntaje_tot += puntaje_parcial + bonus
        print(f"Puntaje de la ronda: {puntaje_tot}")
        print("Turno jugador 2")
        dados_guardados2, bonus2, generala_real2 = turno()
        puntaje_parcial2 = opciones(dados_guardados2, categorias_j2, numeros_j2) 
        puntaje_tot2 += puntaje_parcial2 + bonus2
        print(f"Puntaje de la ronda: {puntaje_tot2}")
    print("Fin del juego")
    if generala_real1 == True:
        print("El Jugador 1 ganó por generala real")
    elif generala_real2 == True:
        print("El Jugador 2 ganó por generala real")
    else:
        print("Planillas completadas.")
        print(f"Puntaje Final Jugador 1: {puntaje_tot1}")
        print(f"Puntaje Final Jugador 2: {puntaje_tot2}")
        if puntaje_tot1 > puntaje_tot2:
            print("Gana el Jugador 1")
        elif puntaje_tot2 > puntaje_tot1:
            print("Gana el Jugador 2")
        else:
            print("empate")


# No cambiar a partir de aqui
if __name__ == "__main__":
    main()
