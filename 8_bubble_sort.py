### 8 Bubble sort
#Implement the bubble sort algorithm.
def run_buble_sort(lst):
    for num in lst :
        
        for x in range(0,len(lst)-1):
            
            if lst[x] > lst[x+1]:
                aux = lst[x]
                lst[x] = lst[x+1]
                lst[x+1] = aux
    return lst


        

if __name__ == '__main__':
    lst = [4,1,6,7,8,8,4,3]
    print(run_buble_sort(lst))





'''
El código que has proporcionado es una implementación del algoritmo Bubble Sort. Veamos si cumple con el algoritmo:

Tienes dos bucles anidados: el bucle externo y el bucle interno. El bucle interno es el que realiza la comparación y el posible intercambio de elementos.

Usas un auxiliar (aux) para hacer el intercambio de elementos si están en un orden incorrecto.

La función run_buble_sort devuelve la lista ordenada.

Sin embargo, hay un pequeño problema con la eficiencia de tu implementación. Aunque el algoritmo funcionará correctamente, no está aprovechando uno de los rasgos característicos del Bubble Sort: después de cada pasada del bucle externo, el elemento más grande (en el caso de orden ascendente) ya estará en su posición correcta al final de la lista. Tu implementación actual no considera esto y siempre itera sobre casi toda la lista con el bucle interno.

Para optimizarlo, puedes modificar el bucle interno para que no considere los elementos que ya están en su posición correcta.'''