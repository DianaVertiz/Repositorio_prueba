# %%
def divide(op1, op2): 
    return op1/op2 # Intentar ingreso de valor no numérico


try:
    op1 = (float(input("Introduce el primer número: ")))            
    op2 = (float(input("Introduce el segundo número: ")))

except ValueError:
    print("El Valor ingresado no es numérico")

else:
    try:
        print(divide(op1, op2))
    except ZeroDivisionError:
        print("No se puede dividir entre 0")
    else:
        print("división realizada con éxito")

finally:
    print("Continua el resto de  mi programa......")