def run_bubble_sort(lst):
    n = len(lst)
    for i in range(n):
        for j in range(0, n-i-1):  # Evitar comparar elementos ya ordenados
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]  # Swap en Python
    return lst

if __name__ == '__main__':
    lst = [4,1,6,7,8,8,4,3]
    print(run_bubble_sort(lst))
