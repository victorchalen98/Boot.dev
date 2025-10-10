def area_sum(rectangles):
    result = 0

    for i in rectangles:
        height = i["height"]
        width = i["width"]
        result += height * width
    return result