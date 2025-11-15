def list_files(parent_directory, current_filepath=""):
    file_paths = []
    for key, value in parent_directory.items():
        new_path = f"{current_filepath}/{key}"
        
        if value == None:
            file_paths.append(new_path)
        else:
            recursive_call = list_files(value, new_path)
            file_paths.extend(recursive_call)
    return file_paths
