import math


class Main:
  
  def mediana(Lista):
    Lista.sort()
    print(Lista)
    resultado = Lista[(int(len(Lista)/2))]
  
    print(resultado)
  
  def pares_inteiros(Lista, x):
    Lista.sort()
    pares = 0
    print(Lista)
    for i in range(0, len(Lista) - 1):
      for j in range(1, len(Lista)):
        if Lista[j] == Lista[i] + x:
          pares += 1
  
    print(pares)

  def grid(texto):
    texto = texto.replace(" ","")
    Lista = list(texto)

    tamanho = math.ceil(math.sqrt(len(Lista)))

    linha = [""] * tamanho

    matriz = [linha] * tamanho
    palavra = []
    cont = 0

    for i in range(0, len(Lista)):
      for j in range(0, tamanho):
        if cont >= tamanho:
          break
        else:
          matriz[i][j] = Lista[cont]
          print("contador: ", cont)
        cont = cont + 1
    
      
    print(matriz)
    
    print(tamanho)
    print(Lista)
    print(matriz)

  grid("tenha um bom dia")

 
    


  

