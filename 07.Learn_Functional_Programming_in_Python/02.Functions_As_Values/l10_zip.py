valid_formats = [
    "docx",
    "pdf",
    "txt",
    "pptx",
    "ppt",
    "md",
]

# Don't edit above this line

def pair_document_with_format(doc_names, doc_formats):
    paired = zip(doc_names, doc_formats)
    
    result = []
    for name, fmt in paired:
        if fmt in valid_formats:
            result.append((name, fmt))
    
    return result
