def find_last_name(names_dict, first_name):
    try:
        return names_dict[first_name]
    except KeyError as e:
        print(f"Error: {e}")
        return None
