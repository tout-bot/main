import discord
import requests

intents = discord.Intents.all()


client = discord.Client(intents=intents)
url = ('https://newsapi.org/v2/everything?'
       'q=Apple&'
       'from=2022-12-21&'
       'sortBy=popularity&'
       'apiKey=keyhere')
response = requests.get(url)
data = response.json()
for article in data['articles']:
            embed = discord.Embed(title=article['title'], description=article['description'])
@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content == '$help':
        await message.channel.send('In dev for now.')
    elif message.content == '$news':
         await message.channel.send(embed=embed)



client.run("tokenhere")
