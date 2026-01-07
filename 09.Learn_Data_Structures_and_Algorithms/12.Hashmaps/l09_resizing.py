class HashMap:
    def insert(self, key, value):
        self.resize()  # SIEMPRE antes de insertar
        index = self.key_to_index(key)
        self.hashmap[index] = (key, value)

    def resize(self):
        # Caso especial: hashmap vacío
        if len(self.hashmap) == 0:
            self.hashmap.append(None)
            return

        load = self.current_load()

        if load < 0.05:
            return

        old_hashmap = self.hashmap
        new_size = len(old_hashmap) * 10
        self.hashmap = [None for _ in range(new_size)]

        for item in old_hashmap:
            if item is not None:
                key, value = item
                index = self.key_to_index(key)
                self.hashmap[index] = (key, value)

    def current_load(self):
        # Si no hay buckets, el load es 1
        if len(self.hashmap) == 0:
            return 1

        filled = 0
        for bucket in self.hashmap:
            if bucket is not None:
                filled += 1

        return filled / len(self.hashmap)

    # don't touch below this line

    def __init__(self, size):
        self.hashmap = [None for i in range(size)]

    def key_to_index(self, key):
        sum = 0
        for c in key:
            sum += ord(c)
        return sum % len(self.hashmap)

    def __repr__(self):
        final = ""
        for i, v in enumerate(self.hashmap):
            if v != None:
                final += f" - {str(v)}\n"
        return final

