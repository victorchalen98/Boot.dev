def count_nested_levels(nested_documents, target_document_id, level=1):
    for doc_id, children in nested_documents.items():
        if doc_id == target_document_id:
            return level

        if isinstance(children, dict) and children:
            found = count_nested_levels(children, target_document_id, level + 1)
            if found != -1:
                return found

    return -1

