from functools import reduce

def join(doc_so_far, sentence):
    return doc_so_far + ". " + sentence

def join_first_sentences(sentences, n):
    if n == 0:
        return ""
    
    first_n = sentences[:n]
    
    combined = reduce(join, first_n)
    
    return combined + "."
