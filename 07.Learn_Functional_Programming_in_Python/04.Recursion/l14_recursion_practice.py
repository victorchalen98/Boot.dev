def find_longest_word(document, longest_word=""):
    if not document.strip():
        return longest_word

    parts = document.split(maxsplit=1)

    first_word = parts[0]
    rest = parts[1] if len(parts) > 1 else ""

    if len(first_word) > len(longest_word):
        longest_word = first_word

    return find_longest_word(rest, longest_word)

