import discord
import asyncio
from settings import token
from commands import commands

client = discord.Client()

botKey = '!tamer'

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.event
async def on_message(message):
    parsed_message = message.content.split(' ', 2)
    if (parsed_message[0] == botKey):
        if len(parsed_message) > 1 and parsed_message[1] in commands:
            await client.send_message(message.channel, commands[parsed_message[1]]())
        else:
            await client.send_message(message.channel, commands['helper']())
            

##        counter = 0
##        tmp = await client.send_message(message.channel, 'Calculating messages...')
##        async for log in client.logs_from(message.channel, limit=10000000):
##            if log.author == message.author:
##                counter += 1
##
##        await client.edit_message(tmp, 'You have {} messages.'.format(counter))

client.run(token)
