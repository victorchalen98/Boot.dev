def get_median_font_size(font_sizes):
    if not font_sizes:
        return None

    sorted_font_sizes = sorted(font_sizes)
    median_len = len(sorted_font_sizes)

    if median_len % 2 == 0:
        median_index = (median_len // 2) - 1
    else:
        median_index = median_len // 2

    median_result = sorted_font_sizes[median_index]
    return median_result
