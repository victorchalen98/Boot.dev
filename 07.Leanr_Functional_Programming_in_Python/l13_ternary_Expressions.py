def choose_parser(file_extension):
    result = "markdown" if file_extension.lower() in ("markdown", "md") else "plaintext"
    return result