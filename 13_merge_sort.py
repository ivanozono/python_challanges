def merge_sort(lst):
    # Si la lista tiene un solo elemento o está vacía, la devolvemos como está
    if len(lst) <= 1:
        return lst

    # Divide la lista en dos partes
    mid_index = len(lst) // 2
    left_half = lst[:mid_index]
    right_half = lst[mid_index:]

    # Llama recursivamente a merge_sort en ambas mitades
    left_sorted = merge_sort(left_half)
    right_sorted = merge_sort(right_half)

    # Combina las dos mitades ordenadas
    return merge(left_sorted, right_sorted)


def merge(left, right):
    result = []
    left_index = 0
    right_index = 0

    # Mientras haya elementos en ambas sublistas
    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            result.append(left[left_index])
            left_index += 1
        else:
            result.append(right[right_index])
            right_index += 1

    # Si aún quedan elementos en la lista izquierda, añádelos al resultado
    while left_index < len(left):
        result.append(left[left_index])
        left_index += 1

    # Si aún quedan elementos en la lista derecha, añádelos al resultado
    while right_index < len(right):
        result.append(right[right_index])
        right_index += 1

    return result


# Prueba del algoritmo
if __name__ == "__main__":
    lst = [14, 7, 3, 12, 9, 11, 6]
    print("Lista original:", lst)
    sorted_lst = merge_sort(lst)
    print("Lista ordenada:", sorted_lst)
