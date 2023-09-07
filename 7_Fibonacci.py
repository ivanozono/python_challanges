## Advanced Functions and Algorithms
### 7 Fibonacci
#Write a function that returns a list with the first n numbers of the Fibonacci sequence.

def fibonacci(n) -> list :
    fibonacci_list = [0,1]
    for x in range(2,n):
        fibonacci_list.append(fibonacci_list[x-2] + fibonacci_list[x-1]) 
    return fibonacci_list


if __name__ == '__main__':
    n = int(input(' Escribe el numero a mostar de la sequence Fibonacci: '))
    print(fibonacci(n))