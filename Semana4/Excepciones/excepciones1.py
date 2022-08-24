


# %%
def divide(op1, op2): #Intentar división por cero
    return op1/op2



op1 = (float(input("Introduce el primer número: ")))            
op2 = (float(input("Introduce el segundo número: ")))

try:
    print(divide(op1, op2))
except ZeroDivisionError:
    print("No se puede dividir entre 0")
else:
    print("división realizada con éxito")
    

print("Continua el resto de  mi programa......")