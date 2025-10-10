def filter_messages(messages):
    filtered_messages = []
    dang_counts = []
    for msg in messages:
        words = msg.split()  
        good_words = []
        dangs = []
        
        for word in words:
            if word == "dang":
                dangs.append(word)  
            else:
                good_words.append(word) 
            
        new_message = " ".join(good_words)
        
        filtered_messages.append(new_message)
        dang_counts.append(len(dangs))
    
    return filtered_messages, dang_counts