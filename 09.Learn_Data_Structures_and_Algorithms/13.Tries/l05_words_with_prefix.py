class Trie:
    def search_level(self, current_level, current_prefix, words):
        if self.end_symbol in current_level:
            words.append(current_prefix)

        for char in sorted(current_level.keys()):
            if char == self.end_symbol:
                continue

            new_prefix = current_prefix + char

            self.search_level(current_level[char], new_prefix, words)

    def words_with_prefix(self, prefix):
        current_level = self.root

        for char in prefix:
            if char not in current_level:
                return []   # No existe ninguna palabra con este prefijo
            current_level = current_level[char]

        words = []
        self.search_level(current_level, prefix, words)
        return words

    # don't touch below this line

    def __init__(self):
        self.root = {}
        self.end_symbol = "*"

    def add(self, word):
        current_level = self.root
        for letter in word:
            if letter not in current_level:
                current_level[letter] = {}
            current_level = current_level[letter]
        current_level[self.end_symbol] = True
