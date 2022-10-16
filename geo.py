
#Importando Bibliotecas

import math
import time
#Lê a imagem
import matplotlib.image as mpimg
#Printa a imagem na tela
import matplotlib.pyplot as plt


#Gerando efeito de espera
def calcular():
  print("Calculando...")
  time.sleep(2)
  


#Definindo loop para programa rodar enquanto o usuário desejar
continuar = True
while continuar:
  print("Escolha um dos polígonos abaixo para calcular: ")

  poligonos = ['Prisma', 'Cubo', 'Paralelepípedo', 'Pirâmide', 'Cone', 'Cilindro', 'Esfera']



  #Mostrando opções de Polígonos
  for i,j in enumerate(poligonos):
    print(f'{i} : {j}')

  #definindo qual polígono será calculado
  poligono = int(input("Escolha uma opção: "))
  
  
  #Prisma 
  if(poligono == 0):
    print("Você escolheu o polígono Prisma!")
    time.sleep(2)
    tipos_prisma = ['Triangular', 'Quadrangular','Pentagonal','Hexagonal']
    for i,j in enumerate(tipos_prisma):
      print(f'{i} : {j}')
      
    prisma = int(input("Escolha uma opção: "))
    
    if(prisma == 0):
      print("Você escolheu o Prisma Triangular!")
      time.sleep(2)
      #Mostrando imagem
      img = mpimg.imread('pt.jpg')
      imgplot = plt.imshow(img)
      plt.show()
      time.sleep(1)
      
      print("0 : Área \n1 : Volume: ")
      opcao = int(input("Você deseja calcular qual das opções acima?: "))
      
      if(opcao == 0):
        base = float(input("Informe o valor da base do Triângulo: " ))
        l2 = float(input("Informe o valor do lado 2 do Triângulo: " ))
        l3 = float(input("Informe o valor do lado 3 do Triângulo: " ))
        ht = float(input("Informe a altura do Triângulo: "))
        hp = float(input("Informe a altura do Prisma: "))
        ab = (base*ht)/2
        al = (base*hp)+(l2*hp)+(l3*hp)
        calcular()
        area_total = 2*ab + al
        print(f"A área total do prisma é {area_total:.2f}u.a")
        
      else:
        base = float(input("Informe o valor da base do Triângulo: " ))
        ht = float(input("Informe a altura do Triângulo: "))
        hp = float(input("Informe a altura do Prisma: "))
        ab = (base*ht)/2
        calcular()
        volume = ab * hp
        print(f"O volume do Prisma Triangular é {volume:.2f}u.v")
        
    elif(prisma == 1):    
      print("Você escolheu o Prisma Quadrangular!")
      time.sleep(2)
      img = mpimg.imread('pq.png')
      imgplot = plt.imshow(img)
      plt.show()
      time.sleep(1)
      print("0 : Área \n1 : Volume: ")
      opcao = int(input("Você deseja calcular qual das opções acima?: "))
      if(opcao == 0):
        lado = float(input("Informe o lado do quadrado: "))
        hp = float(input("Informe a altura do Prisma: "))
        ab = lado*lado
        al = 4*lado * hp
        calcular()
        area_total = 2*ab + al
        print(f"A área total do prisma é {area_total:.2f}u.a")
      else:
        lado = float(input("Informe o lado do quadrado: "))
        hp = float(input("Informe a altura do Prisma: "))
        ab = lado*lado
        calcular()
        volume = ab * hp
        print(f"O volume do Prisma Quadrangular é {volume:.2f}u.v")
        
    elif(prisma == 2):
      print("Você escolheu o Prisma Pentagonal!")
      time.sleep(2)
      img = mpimg.imread('pp.jpg')
      imgplot = plt.imshow(img)
      plt.show()
      time.sleep(1)
      print("0 : Área \n1 : Volume: ")
      opcao = int(input("Você deseja calcular qual das opções acima?: "))
      if(opcao == 0):
        lado = float(input("Informe o lado do pentágono: "))
        hp = float(input("Informe a altura do Prisma: "))
        ab = (5*(lado ** 2))/(4*0.72654252)
        al = 5*lado * hp
        calcular()
        area_total = 2*ab + al
        print(f"A área total do prisma é {area_total:.2f}u.a")
      else:
        lado = float(input("Informe o lado do pentágono: "))
        hp = float(input("Informe a altura do Prisma: "))
        ab = (5*(lado ** 2))/(4*0.72654252)
        calcular()
        volume = ab * hp
        print(f"O volume do Prisma é {volume:.2f}u.v")
        
    elif(prisma == 3):
      print("Você escolheu o Prisma Hexagonal!")
      time.sleep(2)
      img = mpimg.imread('ph.jpg')
      imgplot = plt.imshow(img)
      plt.show()
      time.sleep(1)
      print("0 : Área \n1 : Volume: ")
      opcao = int(input("Você deseja calcular qual das opções acima?: "))
      if(opcao == 0):
        lado = float(input("Informe o lado do hexágono: "))
        hp = float(input("Informe a altura do prisma: "))
        ab = (6*(lado**2)*math.sqrt(3))/4
        al = 6*lado*hp
        calcular()
        area_total = 2*ab + al
        print(f"A área total do prisma é {area_total:.2f}u.a")
        
      else:
        lado = float(input("Informe o lado do hexágono: "))
        hp = float(input("Informe a altura do prisma: "))
        ab = (6*(lado**2)*math.sqrt(3))/4
        calcular()
        volume = ab*hp
        print(f"O volume do Prisma é {volume:.2f}u.v")
        
  #Cubo
  elif(poligono == 1):
    print("Você escolheu o polígono Cubo!")
    time.sleep(2)
    img = mpimg.imread('cubo.jpg')
    imgplot = plt.imshow(img)
    plt.show()
    time.sleep(1)
    print("0 : Área \n1 : Volume: ")
    opcao = int(input("Você deseja calcular qual das opções acima?: "))
    
    if(opcao == 0):
      aresta = float(input("Informe o valor da aresta: "))
      calcular()
      area_total = 6*(aresta**2)
      print(f"A área total do cubo é {area_total:.2f}u.a")
      
    else:
      aresta = float(input("Informe o valor da aresta: "))
      calcular()
      volume = aresta ** 3
      print(f"O volume do cubo é {volume:.2f}u.v")
      
      
  #Paralelepipedo
  elif(poligono == 2):
    print("Você escolheu o polígono Paralelepípedo!")
    time.sleep(2)
    img = mpimg.imread('paralelepipedo.jpg')
    imgplot = plt.imshow(img)
    plt.show()
    time.sleep(1)
    print("0 : Área \n1 : Volume: ")
    opcao = int(input("Você deseja calcular qual das opções acima?: "))
    
    if(opcao == 0):
      comp = float(input("Informe o valor do comprimento: "))
      larg = float(input("Informe o valor da largura: "))
      h = float(input("Informe o valor da altura: "))
      ab = comp * larg 
      x = 2*larg*h
      y = 2 * comp * h
      area_total = 2*ab + x+y
      calcular()
      print(f"A área total do paralelepípedo é {area_total:.2f}u.a")
      
    else:
      comp = float(input("Informe o valor do comprimento: "))
      larg = float(input("Informe o valor da largura: "))
      h = float(input("Informe o valor da altura: "))
      volume = comp * larg * h
      calcular()
      print(f"o volume do paralelepípedo é {volume:.2f}u.v")
      
      
  #Pirâmide
  elif(poligono == 3):
    print("Você escolheu o polígono Pirâmide!")
    time.sleep(2)
    tipos_piramide = ['Triangular', 'Quadrangular','Hexagonal']
    for i,j in enumerate(tipos_piramide):
      print(f'{i} : {j}')
    piramide = int(input("Escolha uma opção: "))
    
    if(piramide == 0):
      print("Você escolheu a Pirâmide triangular!")
      time.sleep(2)
      img = mpimg.imread('piramideT.jpg')
      imgplot = plt.imshow(img)
      plt.show()
      time.sleep(1)
      print("0 : Área \n1 : Volume: ")
      opcao = int(input("Você deseja calcular qual das opções acima?: "))
      if(opcao == 0):
        lado1 = float(input("Informe o valor do lado 1 da base da Pirâmide: "))
        lado2 = float(input("Informe o valor do lado 2 da base da Pirâmide: "))
        lado3 = float(input("Informe o valor do lado 3 da base da Pirâmide: "))
        hi = float(input("Informe a altura inclinada da face lateral: "))
        ht = float(input("Informe a altura do triângulo da base: "))
        ab = (lado1*ht)/2
        al = (lado1*hi)/2 + (lado2*hi)/2 + (lado3*hi)/2
        area_total = ab + al
        calcular()
        print(f"O valor da área total da Pirâmide é {area_total:.2f}u.a")
        
      else:
        lado1 = float(input("Informe o valor do lado 1 da base da Pirâmide: "))
        ht = float(input("Informe a altura do triângulo da base: "))
        hp = float(input("Informe a altura da Pirâmide: "))
        ab = (lado1*ht)/2
        volume = (1/3)*ab*hp
        calcular()
        print(f"O volume da Pirâmide é {volume:.2f}u.v")
        
    if(piramide == 1):
      print("Você escolheu a Pirâmide Quadrangular!")
      time.sleep(2)
      img = mpimg.imread('piramideQ.png')
      imgplot = plt.imshow(img)
      plt.show()
      time.sleep(1)
      print("0 : Área \n1 : Volume: ")
      opcao = int(input("Você deseja calcular qual das opções acima?: "))
      if(opcao == 0):
        lado = float(input("Informe o lado da base: "))
        hi = float(input("Informe a altura inclinada da face lateral: "))
        ab = lado ** 2
        al = ((lado *hi)/2)*4
        area_total = ab + al
        calcular()
        print(f"O valor da área total da Pirâmide é {area_total:.2f}u.a")
        
      else:
        lado = float(input("Informe o lado da base: "))
        hp = float(input("Informe a altura da Pirâmide: "))
        ab = lado ** 2
        volume = (1/3)*ab*hp
        calcular()
        print(f"O volume da Pirâmide é {volume:.2f}u.v")
        
    elif(piramide == 2):
      print("Você escolheu a Pirâmide Hexagonal!")
      time.sleep(2)
      img = mpimg.imread('piramideH.jpg')
      imgplot = plt.imshow(img)
      plt.show()
      time.sleep(1)
      print("0 : Área \n1 : Volume: ")
      opcao = int(input("Você deseja calcular qual das opções acima?: "))
      if(opcao == 0):
        lado = float(input("Informe o lado da base: "))
        hi = float(input("Informe a altura inclinada da face lateral: "))
        ab = (6*(lado**2)*math.sqrt(3))/4
        al = 6*(lado*hi)/2
        area_total = ab + al
        calcular()
        print(f"O valor da área total da Pirâmide é {area_total:.2f}u.a")
        
      else:
        lado = float(input("Informe o lado da base: "))
        hp = float(input("Informe a altura da Pirâmide: "))
        ab = (6*(lado**2)*math.sqrt(3))/4
        volume = (1/3)*ab*hp
        calcular()
        print(f"O volume da Pirâmide é {volume:.2f}u.v")
        
  #Cone
  elif(poligono == 4):
    print("Você escolheu o polígono Cone!")
    time.sleep(2)
    img = mpimg.imread('cone.jpg')
    imgplot = plt.imshow(img)
    plt.show()
    time.sleep(1)
    print("0 : Área \n1 : Volume: ")
    opcao = int(input("Você deseja calcular qual das opções acima?: "))
    
    if(opcao == 0):
      raio = float(input("Informe o raio da base: "))
      g = float(input("Informe o valor da Geratriz: "))
      ab = math.pi * (raio**2)
      al = math.pi * raio * g
      area_total = ab + al
      calcular()
      print(f"O valor da área total do Cone é {area_total:.2f}u.a")
      
    else:
      hc = float(input("Informe a altura do Cone: "))
      raio = float(input("Informe o raio da base: "))
      ab = math.pi * (raio**2)
      volume = (1/3)*ab * hc
      calcular()
      print(f"O volume do Cone é {volume:.2f}u.v")
      
  #Cilindro
  elif(poligono == 5):
    print("Você escolheu o polígono Cilindro!")
    time.sleep(2)
    img = mpimg.imread('cilindro.jpg')
    imgplot = plt.imshow(img)
    plt.show()
    time.sleep(1)
    print("0 : Área \n1 : Volume: ")
    opcao = int(input("Você deseja calcular qual das opções acima?: "))
    
    if(opcao == 0):
      hc = float(input("Informe a altura do cilindro: "))
      raio = float(input("Informe o raio da base: "))
      al = 2*math.pi*raio*hc
      ab = 2*(math.pi*(raio**2))          
      area_total = ab + al
      calcular()
      print(f"O valor da área total do Cilindro é {area_total:.2f}u.a")
      
    else:
      hc = float(input("Informe a altura do cilindro: "))
      raio = float(input("Informe o raio da base: "))
      volume = math.pi * (raio ** 2) * hc
      calcular()
      print(f"O volume do Cilindro é {volume:.2f}u.v")
      
  #Esfera
  elif(poligono == 6):
    print("Você escolheu o polígono Esfera!")
    time.sleep(2)
    img = mpimg.imread('esfera.png')
    imgplot = plt.imshow(img)
    plt.show()
    time.sleep(1)
    print("0 : Área \n1 : Volume: ")
    opcao = int(input("Você deseja calcular qual das opções acima?: "))
    
    if(opcao == 0):
      raio = float(input("Informe o valor do raio: "))
      area_total = 4*math.pi * (raio**2)
      calcular()
      print(f"O valor da área total da Esfera é {area_total:.2f}u.a")
      
    else:
      raio = float(input("Informe o valor do raio: "))
      volume = (4/3)*math.pi*(raio**3)
      calcular()
      print(f"O volume da Esfera é {volume:.2f}u.v")
      
  
  else:
    print("Opção invlálida! Escolha uma opção disponível!")
  
  #verificando se usuário deseja continuar
  time.sleep(2)
  continuar = int(input("Você deseja continuar? \n 0 - SIM \n 1 - NÂO:\n "))
  if(continuar == 1):
    continuar = False
    print("Encerrando...")
    time.sleep(2)
  else:
    continuar = True
    print("Reiniciando...")
    print("\n")
    
    time.sleep(2)
    
  
  
print("Fim da execução!")
          
                  
  
      
      

"""
  print(" 0 : Prisma") 
  print(" 1 : Cubo") 
  print(" 2 : Paralelepípedo") 
  print(" 3 : Pirâmide") 
  print(" 4 : Cone") 
  print(" 5 : Cilindro")
  print(" 6 : Esfera") 
"""
      
    
      
        
        
      