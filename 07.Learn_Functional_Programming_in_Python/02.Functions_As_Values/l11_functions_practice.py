def restore_documents(originals, backups):
    combined = originals + backups
    cleaned = []
    for doc in combined:
        if not doc.isdigit():
            cleaned.append(doc.upper())
    return set(cleaned)
