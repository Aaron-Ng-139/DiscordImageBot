import json
import discord
import responses

async def send_message(discord, message, user_message, is_private):
    try:
        response = responses.handle_response(discord, user_message)
        if is_private:
            await message.author.send(response)
        elif isinstance(response, str):
            await message.channel.send(response)
        elif isinstance(response, discord.File):
            await message.channel.send(file=response)
    except Exception as e:
        print(e)
    
def run_discord_bot():
    
    # Get bot token from json file
    f = open('botConfig.json')
    data = json.load(f)
    TOKEN = data["DISCORD_BOT_TOKEN"]
    f.close()
    
    client = discord.Client(intents=discord.Intents.all())
    
    # Startup message
    @client.event
    async def on_ready():
        print(f'{client.user} is now running!')
        
    # User messsage handling
    @client.event
    async def on_message(message):
        if message.author == client.user:
            return 
            
        username = str(message.author)
        user_message = str(message.content)
        channel = str(message.channel)
        
        print (f"{username} said '{user_message}' ({channel})")
        
        if user_message[0] == "$":
            user_message = user_message[1:]
            await send_message(message, user_message, is_private=False)
    
    client.run(TOKEN)