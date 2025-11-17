def lines_with_sequence(char):
    def with_char(length):
        sequence = char * length
        def with_length(doc):
            line_number = 0
            doc_lines = doc.split("\n")
            for docs in doc_lines:
                if sequence in docs:
                    line_number += 1
            return line_number
        return with_length
    return with_char
