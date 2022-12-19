import discord #import discord library
import os
from keep_alive import keep_alive

client = discord.Client() #create an instance of a client which will connect to disc 

@client.event #use our client.event decorator to register an event 

#when bot is rdy to use, call this
async def on_ready(): 
  print('We have logged in as {0.user}'.format(client))

#create an event if our bot senses a message in the sergver
@client.event
async def on_message(message):
  if message.author == client.user: #if author of msg of the bot user, then return
    return
  if message.content.startswith('!xD'):
    await message.channel.send("xD")

keep_alive()#run our webserver

client.run(os.getenv('TOKEN')) #let the client get our token from our .env file