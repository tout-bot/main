import discord
import requests

client = discord.Client()

@client.event
async def on_ready():
    print(f'Successfully logged in as {client.user}')
