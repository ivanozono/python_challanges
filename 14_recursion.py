def fibonacci(n):
    # Casos base
    if n == 0:
        return 0
    elif n == 1:
        return 1

    # Llamada recursiva para los términos n-1 y n-2
    return fibonacci(n-1) + fibonacci(n-2)


# Prueba de la función
if __name__ == "__main__":
    n = int(input("Introduce el valor de n: "))
    print(f"El {n}-ésimo término de la secuencia de Fibonacci es: {fibonacci(n)}")
