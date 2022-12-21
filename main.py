import discord
import requests

client = discord.Client()

@client.event
async def on_ready():
    print(f'Successfully logged in as {client.user}')

#if ur not going to add commands then remove this
@client.event
async def on_message(message):
    #it checks if the bot itself sent the message and will ignore it
    if message.author == client.user:
        return
