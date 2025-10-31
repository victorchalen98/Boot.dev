def add_prefix(document, documents):
    prefix = f"{len(documents)}. "
    new_doc = prefix + document
    documents.append(new_doc)
    return documents
