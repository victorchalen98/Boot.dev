def get_avg_brand_followers(all_handles, brand_name):
    total = 0
    for handles in all_handles:
        for h in handles:
            if brand_name in h:
                total +=1
    if len(all_handles) == 0:
        return 0
    
    return round(total / len(all_handles), 2)

