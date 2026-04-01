import discord
import random
import os

def run_discord_bot():
    TOKEN = os.getenv("DISCORD TOKEN")

    intents = discord.Intents.default()
    intents.message_content = True

    client = discord.Client(intents=intents)

    @client.event
    async def on_ready():
        print(f"{client.user} is now running")
    
    @client.event
    async def on_message(message):
        if message.author == client.user:
            return
        
        content = message.content.strip()
