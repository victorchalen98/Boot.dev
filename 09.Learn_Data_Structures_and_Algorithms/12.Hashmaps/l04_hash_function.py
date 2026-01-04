class HashMap:
    def key_to_index(self, key):
        input = key
        sum = 0
        
        for c in input:
            sum += ord(c)

        result = sum % len(self.hashmap)

        return result

    # don't touch below this line

    def __init__(self, size):
        self.hashmap = [None for i in range(size)]

    def __repr__(self):
        buckets = []
        for v in self.hashmap:
            if v != None:
                buckets.append(v)
        return str(buckets)

