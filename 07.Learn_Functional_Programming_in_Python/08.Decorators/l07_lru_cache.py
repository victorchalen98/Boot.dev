from functools import lru_cache

@lru_cache()
def is_palindrome(word: str) -> bool:
    # Normalizamos para evitar problemas con mayúsculas
    word = word.lower()

    # Caso base: palabras de longitud 0 o 1 son palíndromos
    if len(word) <= 1:
        return True

    # Si los extremos no coinciden, no es palíndromo
    if word[0] != word[-1]:
        return False

    # Recursión moviéndonos hacia adentro
    return is_palindrome(word[1:-1])
