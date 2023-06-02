import random

# Response handler
def handle_response(msg) -> object:
    text = msg.lower()
    
    if text == 'ahoy':
        return 'ahoy!'
       
    if text == "help":
        return """
        `Bot Commands: \n(rand #min #max) Outputs random integer between #min (inclusive) and #max (exclusive)`
        """
    
    # Rolling a random integer
    if text[:5] == "rand ":
        return random_integer(text)
    
    # Random image
    if text == "img":
        links = ['https://i.imgur.com/Z7IiErH.png', 'https://i.imgur.com/pyCNHvE.png']
        return links[random.randint(0, len(links)-1)]
        # return discord.File("a.png")
        
def random_integer(text):
    """Returns random  integer between two given numbers
    
    Args:
        text: user message, ideally formatted correctly
    
    Returns:
        Integer between given min and max (inclusive)
    """
    text = text[5:].split()
    if len(text) != 2:
        return "Error: rand only takes 2 numerical arguments (rand #min #max)"
    try:
        num_min = int(text[0])
        num_max = int(text[1])
    except ValueError:
        return "Error: rand needs 2 integers (rand #min #max)"
    if num_min > num_max:
        return "Error: max cannot be less than min (rand #min #max)"
    return random.randint(num_min, num_max)