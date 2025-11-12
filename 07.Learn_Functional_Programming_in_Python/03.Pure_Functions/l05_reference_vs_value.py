def add_format(default_formats, new_format):
    copy_new_format = default_formats.copy()    
    copy_new_format[new_format] = True
    return copy_new_format


def remove_format(default_formats, old_format):
    copy_old_format = default_formats.copy()
    copy_old_format[old_format] = False
    return copy_old_format
