import random
while True:
   input("Nyomj egy ENTERT a dobáshoz")

   num = random.randint(1,11)
   print("A szám amit kaptál:",num)
   option = input("Újra dobsz?(Igen/Nem) ")

   if option == 'Nem':
       break