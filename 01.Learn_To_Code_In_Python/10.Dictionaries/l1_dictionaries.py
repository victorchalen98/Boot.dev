def get_character_record(name, server, level, rank):
    id = (f"{name}#{server}")
    return {
        "name": name,
        "server": server,
        "level": level,
        "rank": rank,
        "id": id
    }


