### 5 Palindrome
## Write a function that checks if a given string is a palindrome.

def palindrome(word) -> bool :
    if word[::] == word[::-1] :
        palindrome_word = True
    else :
        palindrome_word = False
    return palindrome_word



if __name__ == "__main__":
    word = str(input("Escribe una palabra: "))
    result = palindrome(word)
    print(result)