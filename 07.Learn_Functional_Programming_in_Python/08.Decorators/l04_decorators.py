def markdown_to_text_decorator(func):
    def wrapper(*args, **kwargs):
        new_args = [convert_md_to_txt(arg) for arg in args]

        new_kwargs = {k: convert_md_to_txt(v) for k, v in kwargs.items()}

        return func(*new_args, **new_kwargs)

    return wrapper


# don't touch below this line


def convert_md_to_txt(doc):
    lines = doc.split("\n")
    for i in range(len(lines)):
        line = lines[i]
        lines[i] = line.lstrip("# ")
    return "\n".join(lines)
