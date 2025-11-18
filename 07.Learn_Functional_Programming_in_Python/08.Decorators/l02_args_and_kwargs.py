def args_logger(*args, **kwargs):
    for i, args in enumerate(args, start=1):
        print(f"{i}. {args}")

    for key, value in sorted(kwargs.items()):
        print(f"* {key}: {value}")
        
        

args_logger("hi", "there", age=17, date="July 4 1776")
