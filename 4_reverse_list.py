## List and String Manipulation
### 4 Reverse a list
#Write a function that takes a list and returns it reversed.

def main(list):
    reverselist = list[::-1]
    print(reverselist)


if __name__ == "__main__":
    entry = input ('Escribe numeros separas por espacios: ')
    list = [int(x) for x in entry.split()] # convertir la cadena de entrada en una lista de numeros
    main(list)