import discord
import asyncio
from settings import token, WELCOME_MESSAGE, CHANNEL
from commands import commands

client = discord.Client()

botKey = '!t'

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('Finding a server to say hello...')
    channels = client.get_all_channels()
    channel = None
    for chan in channels:
        if chan.name == CHANNEL:
            channel = chan
    if (channel is not None):
        await client.send_message(channel, "Hello channel :).")
        print ('... and sent hello to one :).')
    else:
        print ('... but couldn\'t find any :(.')
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

if __name__ == '__main__':
    client.run(token)
