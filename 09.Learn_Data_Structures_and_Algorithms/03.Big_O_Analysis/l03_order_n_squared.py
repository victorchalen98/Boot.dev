def does_name_exist(first_names, last_names, full_name):
    for firts in first_names:
        for last in last_names:
            if f"{firts} {last}" == full_name:
                return True
                
    return False
