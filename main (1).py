numero1 = int(input("Ingrese el primer número:"))
numero2 = int(input("Ingrese el segundo número:"))

numeros_primo={2,3,5,7}
diferencia = numero1-numero2

if diferencia %2==0:
    print("Se divide entre dos y suma es:", numero1 + numero2)
if diferencia < 10 and diferencia in numeros_primo:
    print("es primo y su producto es:", numero1 *numero2)
diferencia_string = str(diferencia)
if diferencia_string[-1] == '4':
      print("Termina en 4 y sus dígitos son:")
      for numero in diferencia_string:
        print(numero)