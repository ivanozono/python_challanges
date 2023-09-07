
def binary_search(num,lst) -> bool:
    low = 0
    high = len(lst)-1

    while low <= high :
        median = (low + high) // 2

        if num == lst[median]:
            return print("Si se encuentra el elemento !!! ")
        elif lst[median] < num :
            low = median + 1
        elif lst[median] > num :
            high = median - 1

    return print("No se encontro")




    


if __name__ == '__main__':
    num = int(input("Escribe el numero a buscar: ")) 
    lst = [2,6,8,9]
    binary_search(num,lst)