default_commands = {}
default_formats = ["txt", "md", "html"]
saved_documents = {}

# Don't edit above this line


def add_custom_command(commands, new_command, function):
    new_commands = commands.copy()
    new_commands[new_command] = function
    return new_commands


def add_format(formats, format):
    new_formats = formats.copy()
    new_formats.append(format)
    return new_formats


def save_document(docs, file_name, doc):
    new_docs = docs.copy()
    new_docs[file_name] = doc
    return new_docs


def add_line_break(line):
    new_line = (line + "\n\n")
    return new_line