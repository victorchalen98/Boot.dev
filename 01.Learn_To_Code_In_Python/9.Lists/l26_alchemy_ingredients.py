def check_ingredient_match(recipe, ingredients):
    missing = []  
    
    for item in recipe:
        if item not in ingredients:
            missing.append(item)
    
    have = len(recipe) - len(missing)
    
    if len(recipe) > 0:
        percentage = (have / len(recipe)) * 100
    else:
        percentage = 0.0
    
    return percentage, missing
