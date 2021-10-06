def add_numbers(x,y):
   sum = x + y
   return sum
def subt_numbers(x,y):
    subt = x - y
    return subt
def multi_numbers(x,y):
    multi = (x*y)
    return multi
def div_numbers(x,y):
    div = (x/y)
    return div
num1 = float(input("num1: "))
num2 = float(input("num2: "))
op = int(input("operation: 1:sum, 2:subtract, 3:multiplication, 4:divison  "))
if op == 1:
    print("The sum is", add_numbers(num1, num2))
elif op == 2:
    print("The subt. is", subt_numbers(num1, num2))
elif op == 3:
    print("The multi. is", multi_numbers(num1, num2))
elif op == 4:
    print("The div. is", div_numbers(num1, num2))
else:
    print("unknown operation")