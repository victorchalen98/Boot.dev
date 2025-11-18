def create_markdown_image(alt_text):
    text = f"![{alt_text}]"
    def string_input(url):
        sequence_url_1 = url.replace("(", "%28")
        sequence_url_2 = sequence_url_1.replace(")", "%29")
        enclose_url = f"({sequence_url_2})"
        text_url = text + enclose_url

        def get_title(title=None):
            final_text = ""
            if title:
                text_title = f'"{title}"'
                nonlocal text_url
                text_url_rep = text_url.replace(")"," ")
                final_text = f"{text_url_rep}{text_title})"
                return final_text
            else: 
                final_text = f"{text_url}"
                return final_text

        return get_title
    return string_input
