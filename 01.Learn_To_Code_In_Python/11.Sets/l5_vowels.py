def count_vowels(text):
    vowels_set = {"A", "E", "I", "O", "U", "a", "e", "i", "o", "u"}
    counter = 0
    unique_vowels = set()

    for vocales in text:
        if vocales in vowels_set:
            counter +=1
            unique_vowels.add(vocales)
    


    return (counter, unique_vowels)


