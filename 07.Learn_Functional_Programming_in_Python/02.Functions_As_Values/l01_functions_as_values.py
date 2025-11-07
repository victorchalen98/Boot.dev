def file_to_prompt(file, to_string):
    formatted_string = to_string
    promp = formatted_string(file)
    result = (f"```\n{promp}\n```")
    return result