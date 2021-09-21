import discord
from discord.ext import tasks
import os
import requests
import json
from keep_alive import keep_alive
from random import choice


client=discord.Client()

status = ['Jamming out to Quotes!', 'Eating!', 'Sleeping!']

def get_quote():
  response = requests.get("https://zenquotes.io/api/random")
  json_data = json.loads(response.text)
  quote = json_data[0]['q'] + " -" + json_data[0]['a']
  return(quote)

'''def get_dog_image():
  response = requests.get("https://dog.ceo/api/breeds/image/random")
  json_data = json.loads(response.text)
  url=json_data["message"]
  return(url)'''

@client.event
async def on_ready():
  ##await client.change_presence(activity=discord.Game("Hello There!"))
  change_status.start()
  print('we have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  if message.content.startswith('$inspo'):
    quote = get_quote()
    await message.channel.send(quote) 

  '''if message.content.startswith('$dog'):
    dog=get_dog_image()
    embed=discord.Embed(color = discord.Colour.red())
    embed.set_image(url = dog)
    await message.channel.send(embed=embed)'''

@tasks.loop(seconds=20)
async def change_status():
    await client.change_presence(activity=discord.Game(choice(status)))

keep_alive()
client.run(os.getenv('TOKEN'))