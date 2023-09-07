### 6 Frequency of elements
# Write a function that takes a list and returns a dictionary with the frequency of each element in the list.

def frequency_element(list) -> dict :
    
    frec_dict = {}

    for item in list :
        if item in frec_dict:
           frec_dict[item] += 1
        else:
            frec_dict[item] = 1
    return frec_dict



if __name__ == "__main__":
    elementos = str(input("Escribe elements separados por espacio: "))
    list = [int(x) for x in elementos.split()]
    print(frequency_element(list))
    