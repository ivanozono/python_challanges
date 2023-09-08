### 11 Maximum and minimum
#Write functions that find the maximum and minimum value in a list of numbers.

def fun_max_min(lst):
    max_lst = max(lst)
    min_lst = min(lst)
    return (max_lst, min_lst) 



if __name__ == '__main__':
    lst = [8, 9, 89, 2, 32]
    max_lst, minlst = fun_max_min(lst)
    print( f"El maximo es {max_lst} y el minimo es {minlst}")