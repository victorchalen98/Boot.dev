def file_type_getter(file_extension_tuples):
    extension_to_type = {}

    for file_type, extensions in file_extension_tuples:
        for ext in extensions:
            extension_to_type[ext] = file_type

    return lambda ext: extension_to_type.get(ext, "Unknown")
