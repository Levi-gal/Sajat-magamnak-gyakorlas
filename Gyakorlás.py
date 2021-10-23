import random
szavak = ["Arany tömb" , "Gyémánt" , "Cseresznye" , "Pénzes zsák" , "Kard"]
int(input("Üss be egy 1-est a kezdéshez "))

num1 = random.choice(szavak)
num2 = random.choice(szavak)
num3 = random.choice(szavak)
print("Az tárgy amit kaptál:",num1)
print("Az tárgy amit kaptál:",num2)
print("Az tárgy amit kaptál:",num3)

if(num1 == num2 == num3):
    print("Max nyeremény: 5000Ft")

elif(num1 == num2):
    print("Közepes nyeremény: 2500Ft")

elif(num1 == num3):
    print("Közepes nyeremény: 2500Ft")

elif(num2 == num3):
    print("Közepes nyeremény: 2500Ft")

else:
    print("Nem nyert")
