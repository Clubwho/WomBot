import discord      #Imports discords commands
import asyncio      #Imports asyncio's commands

client = discord.Client()   #Sets makes discord.Client() smaller

#Say who it is when logging in (not is discord)
@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

#Simple reply
@client.event
async def on_message(message):
    #Posts a picture of yee
    if message.content.startswith('yee!'):
        await client.send_message(message.channel, 'http://i.imgur.com/SdM4EME.png')
    #Posts the lenny face
    if message.content.startswith('lenny'):
        await client.send_message(message.channel, '( ͡° ͜ʖ ͡° )')
    #Posts a gif of wow
    if message.content.startswith(('wow!' , 'wew!')):
        await client.send_message(message.channel, 'http://i.imgur.com/Mj2iT9d.gif')
    #Posts keem dancing to numa numa
    if message.content.startswith('keem!'):
        await client.send_message(message.channel, 'https://www.youtube.com/watch?v=tuCi9_dfntg&index=34&list=WL')
    #Posts Go Aussie Go
    if message.content.startswith('straya'):
        await client.send_message(message.channel, 'https://www.youtube.com/watch?v=mZ3Ihas3ouw')
    #Posts I sexually identify as an attack helicopter
    if message.content.startswith('attack helicopter'):
        await client.send_message(message.channel, 'https://www.youtube.com/watch?v=WPMDCJrRpT8')
    #Posts the lenny face
    if message.content.startswith('oi cunt you there?'):
        await client.send_message(message.channel, 'oh yeah cunt I am here')

#Reply with argument
@client.event
async def on_message(message):
    

#Google Translate
@client.event
async def on_message(message)


#https://discordapp.com/oauth2/authorize?client_id=205653889624571905&scope=bot&permissions=0
client.run('Token')
