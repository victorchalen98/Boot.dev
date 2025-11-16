def word_count_aggregator():
    count = 0
    def number_of_words(doc):
        result = len(doc.split(" "))
        nonlocal count
        count += result 
        return count
    return number_of_words
