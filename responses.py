def handle_response(msg) -> str:
    text = msg.lower()
    
    if text == 'hello':
        return 'hello world!'
       
    if text == "help":
        return "`help message`"
    
    return "default response"