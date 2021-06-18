import discord
import os
from discord.ext import commands

client = commands.Bot(command_prefix='p!')



@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('hello'):
        await message.channel.send('Hello!')


@client.event
async def on_voice_state_update(member, before, after):
    channel = after.channel
    bot_connection = member.guild.voice_client
    print(str(channel) + "    " + str(member.id))

client.run(os.getenv('TOKEN'))

# Simple bot that replies to hello messages.
# Future methods will be added below
