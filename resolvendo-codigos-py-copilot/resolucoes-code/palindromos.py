def is_palindrome(word):
    reversed_word = word[::-1]
    if word == reversed_word:
        return True
    else:
        return False

word = input("Digite uma palavra: ")
if is_palindrome(word):
    print("A palavra é um palíndromo!")
else:
    print("A palavra não é um palíndromo.")