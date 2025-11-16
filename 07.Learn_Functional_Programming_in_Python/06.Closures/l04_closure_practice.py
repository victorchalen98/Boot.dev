def new_collection(initial_docs):
    docs_copy = initial_docs.copy()
    def append_list(document):
        docs_copy.append(document)
        return docs_copy
    
    return append_list
