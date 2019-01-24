import discord
import asyncio
from settings import token, WELCOME_MESSAGE, CHANNEL
from commands import commands

client = discord.Client()

bot_trigger = "!t"


@client.event
async def on_ready():
    print("Logged in as")
    print(client.user.name)
    print(client.user.id)
    print("Finding a server to say hello...")
    channels = client.get_all_channels()
    channel = None
    for chan in channels:
        if chan.name == CHANNEL:
            channel = chan
    if channel is not None:
        await client.send_message(channel, WELCOME_MESSAGE.format(channel.mention))
        print("... and sent hello to one :).")
    else:
        print("... but couldn't find any :(.")
    print("------")


@client.event
async def on_message(message):
    parsed_message = message.content.split(" ", 2)
    if parsed_message[0] == bot_trigger:
        if len(parsed_message) > 1:
            await client.send_message(
                message.channel,
                commands.get(parsed_message[1])(
                    parsed_message[2] if len(parsed_message) > 2 else None
                ),
            )


from dbmanagement import setup_db
from models import *

if __name__ == "__main__":
    setup_db()
    client.run(token)
