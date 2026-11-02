import random 
x = random.randint(1,10)
n = 1 
print("Hej!")
name = input("Vad heter du? ")
print(f"hej {name} välkommen till spelet ! \n gissa talet mellan 1 och 10:")
while True:
   gissning = int(input(f"Försök {n} Gissa talet: "))
   print(gissning)
   if gissning == x:
      print("bra jobbat du gissade rätt tal")
      break
   else:
      print("fel gissat")
      n+=1