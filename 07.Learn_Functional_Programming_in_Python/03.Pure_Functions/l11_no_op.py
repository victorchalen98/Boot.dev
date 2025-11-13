def remove_emphasis(document):
    new_document = document
    lines = new_document.split("\n")
    new_lines = map(remove_line_emphasis, lines)
    new_document = "\n".join(new_lines)
    return new_document


# Don't touch below this line


def remove_line_emphasis(line):
    words = line.split()
    new_words = map(remove_word_emphasis, words)
    return " ".join(new_words)


def remove_word_emphasis(word):
    return word.strip("*")
