import random

bandas= []
banda ={}

opcion  = None
while(opcion != 5):
  try:
    print("FESTIVLA ALTAVOZ")
    print("********************************")
    print("1.Registrar banda")
    print("2.Cartel festival")
    print("3.Buecar banda")
    print("4.Modificar bonda")
    print("5.Finalizar")  
    opcion= int(input("Diguites una opcion: "))
    
    if opcion == 1:
      banda = {}
      #se pide las caracteristica de la banda 
      banda["idBanda"]=random.randint(999,1000)
      banda["nombreBanda"]= input("ingrese el nembre de la banda: ")
      banda["generoBanda"]= input("ingrese el generode la banda de la banda: ")
      banda["calsificacion"]= input("cual es la calsificacion de la banda: ")
      bandas.append(banda)
      # como agrego un dicionario a un a lista 
      
    elif opcion == 2:
      for bandaAuxiliar in bandas:
        print(f'{bandaAuxiliar} -- {bandaAuxiliar["nombreBanda"]}')
    elif opcion == 3:
      #buscando una banda en mi arreglo 
      bandabuscada = input('dijite el nombre de la banda: ')
      for banadaAuxiliar in bandas:
        if bandaAuxiliar["nombreBanda"]== bandabuscada:
          print(f'oe, si esta ')
        else:
          ("no mano eso no es, no esta")
    elif opcion == 4:
      pass
    elif opcion == 5:
      pass
  except ValueError:
    print("solo se admite numeros")
