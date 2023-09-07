## 3 Factorial
# Write a function that calculates the factorial of a given number.

def main(num):
    fact = 1
    for i in range(1, num + 1):
        fact = fact * i
    print(fact)


if __name__ == "__main__":
    num=int(input("Enter the number: "))
    main(num)