def doc_format_checker_and_converter(conversion_function, valid_formats):
    def file_extension(filename, content):
        extension = filename.split(".")
        if extension[1] in valid_formats:
            return conversion_function(content)
        else:
            raise ValueError("invalid file format")
    return file_extension


# Don't edit below this line


def capitalize_content(content):
    return content.upper()


def reverse_content(content):
    return content[::-1]
