def calculus(func):
    
    def wrapper(obj):
        print("El resultado es: ", end=" ")
        resultado = func()
        print(resultado)
        print("-" * 30)
        return resultado
    
    return wrapper

def funcion_decoradora(funcion):
    def suma_plus(a,b):
        if a != b:
            resultado = 2 * funcion(a,b)
        else:
            resultado = funcion(a,b)  
        return resultado
    return suma_plus

@funcion_decoradora
def suma(a,b):
    return a+b

print(suma(1,3))