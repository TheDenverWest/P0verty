    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
   # Author: Harm
  # 12/16/2022 
 # This is a discord bot which will respond to inputs with images or gifs
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
import discord
import os
import datetime
import random
from keep_alive import keep_alive 

     # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # intents are necessary after sep '22 we will define them manually:
   # https://discordpy.readthedocs.io/en/latest/intents.html?highlight=intents
  # the message_content intent is special, ensure that it is turned on in the developer app 
 # https://discord.com/developers/applications/1053186050857639996/bot
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
intents = discord.Intents.default()
intents.typing = False
intents.presences = False
intents.message_content = True 

client = discord.Client(intents=intents)

kirkdict = {
  "kirk1" : "https://imgur.com/VbgdMtL",
  "kirk2" : "https://imgur.com/ZDxic5n",
  "kirk3" : "https://imgur.com/iai4oU1"
}

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
 # This area defines the events that the bot will listen to
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
@client.event
async def on_ready():
  print('Logged in as {0.user}'.format(client))
startTime = datetime.datetime.utcnow()

@client.event
async def on_message(message):

  if message.author == client.user:
    return  # do nothing if the message is from the bot

  msg = message.content

  #gm00t
  if "gm00t" in msg:
     await message.channel.send('https://imgur.com/RMIW6sp')

  #gm00t
  if "frank" in msg and ":frank:" not in msg:
     await message.channel.send('https://imgur.com/RMIW6sp')
  
  #spit
  if "!spit" in msg:
     await message.channel.send('https://tenor.com/view/spit-gif-22259405')
    
  #poor
  if "!poor" in msg:
     await message.channel.send('https://media.tenor.com/cLM08U_moEIAAAAC/elizabeth-taylor-poor.gif')

  #violet
  if "!violet" in msg:
     await message.channel.send('https://cdn.discordapp.com/attachments/1052447227370553344/1053343139827552306/25941542.gif')

  #jfc
  if "!jfc" in msg:
     await message.channel.send('https://imgur.com/a/slhbSjS')

  #bottom signal
  if "bottom signal" in msg:
     await message.channel.send('https://tenor.com/view/downs-down-syndrome-huh-look-back-what-gif-12361802')
  
  #kirk
  if "kirk" in msg:
     kirkrand = random.choice(list(kirkdict.values()))
     await message.channel.send(kirkrand)
    
  #uptime
  if "!uptime" in msg:
     upTime = datetime.datetime.utcnow() - startTime
     await message.channel.send(f'bot has been live for: {upTime}')
    
        # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
       #       the below portion is very important since this code is public.
      # Never ever expose the token to anyone, do not paste it in the code, always pass by ref
     # the keep alive function will allow us to stay awake even when there are no inputs for hours
    # this utilizes uptimerobot https://uptimerobot.com/dashboard.php#mainDashboard
   #       On reate limits:
  # # Don't use repl.it as your host. They use a shared IP for everything running on the service, if someone gets banned on discord, everyone on that IP will 
 # be # banned. Including you. – 
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

keep_alive()
client.run(os.getenv('token'))