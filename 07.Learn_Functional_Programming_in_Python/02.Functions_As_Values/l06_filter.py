def remove_invalid_lines(document):
    lines = document.split("\n")  
    valid_lines = filter(lambda line: not line.startswith("-"), lines)  
    return "\n".join(valid_lines)  
