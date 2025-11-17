import copy
def css_styles(initial_styles):
    copy_styles = copy.deepcopy(initial_styles)

    def add_style(selector, property, value):
        nonlocal copy_styles
        if selector not in copy_styles:
            new_dic = {}
            new_dic.update({property: value})
            copy_styles[selector] = new_dic
        else:
            copy_styles[selector].update({property: value})

        return copy_styles   

    return add_style  

