import random 
import datetime as  time 





dibujo = dibujo= [
    '''
        +---+
        |   |
            |
            |
            |
            |
            ============''', 
            '''
        +---+
        |   |
        O   |
            |
            |
            |
            ============''', 
            '''
        +---+
        |   |
        O   |
        |   |
            |
            |
            ============''', 
            '''
        +---+
        |   |
        O   |
        |\  |
            |
            |
            ============''',
            '''
        +---+
        |   |
        O   |
       /|\  |
            |
            |
            ============''',
            '''
        +---+
        |   |
        O   |
       /|\  |
         \  |
            |
            ============''',
            '''
        +---+
        |   |
        O   |
       /|\  |
       / \  |
            |FAILED
            ============'''
]

oraciones = '''andrs felipe ramirex'''

def encuentra_palabra():
    
    palabra = oraciones.split()##con esplit lo que hacemos es que de un string tome todos los valores y los convierta en una lista y los convierta en string 
    #n =random.randint(palabra)# este  no dara error
    n = random.randint(0 , len(palabra) -1) # el menos sse le pone porque se empieza desde cero entonce el primer nombre no cuenta como numero 
    return palabra[n] # este nos dice palabras al azar 

def main(): 
    palabra = encuentra_palabra() # este nos da la palabra 
    lista_palabra= []
    lista2_palabra = []
    for i in palabra : # este lee cada letra  de la palabra    encontrada 
        lista_palabra.append(i)
        lista2_palabra.append('___')

    contadorDibujo = 0
    print(dibujo[contadorDibujo])
    print(lista_palabra)
    print(','.join(lista2_palabra)) #join sirve para  que cojauna lista , le quite los parentesis  y printe los guiones sin parentesis y con comas 

    while True:
        llave = False
        entrada = input('\n ingrese  una letra ')
        contador = -1
        

        for i in palabra: 
            contador +=1
            if entrada == i : 
                lista2_palabra[contador] = entrada 
                llave==True
        if lista_palabra == lista2_palabra : 
            print('\n adivinaste  la palabra ')
            print('ganaste, la palabra era : ', ''.join(lista_palabra))
            print(palabra)
            break
        if contadorDibujo >= 5 and llave != True:
            print(dibujo[6])
            print('perdiste la palbra correcta es :', ''.join(lista_palabra))
            break

        elif llave != False:
            contadorDibujo += 1

        print(dibujo[contadorDibujo])
        print(','.join(lista2_palabra)) #j

main()
