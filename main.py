nombre=input("¿Cómo te llamas?")
vocales=["a","e","i","o","u"]
i=0
while True:
  for vocal in nombre:
    if vocal in vocales:
       i=i+1
  if i>=3:
    print("tu nombre tiene",i, "vocales", "y su nombre es:", nombre)
    break
  else: 
    print("intentalo de nuevo")
    print("tu nombre no tiene 3 o más vocales")
    nombre=input("¿Cómo te llamas?")
    i=0

