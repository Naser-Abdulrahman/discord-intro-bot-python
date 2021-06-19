import time
import discord
import os
from discord.ext import commands
from discord import FFmpegPCMAudio


class Botty:
    def __init__(self, token=None):
        self.client = commands.Bot(command_prefix='p!')
        self.is_connected = False
        self.on_ready = self.client.event(self.on_ready)
        self.on_message = self.client.event(self.on_message)
        self.on_voice_state_update = self.client.event(self.on_voice_state_update)
        self.token = token or os.getenv('TOKEN')

    async def on_ready(self):
        print('We have logged in as {0.user}'.format(self.client))

    async def on_message(self, message):
        if message.author == self.client.user:
            return

        if message.content.startswith('hello'):
            await message.channel.send('Hello!')

    async def on_voice_state_update(self, member, before, after):
        if before is not None:
            print('before!')
            chann = before.channel
        else:
            print('After!')
            chann = after.channel
        bot_connection = member.guild.voice_client

        print('true')
        if str(member.nick) == "Test1":
            if bot_connection:
                await bot_connection.move_to(chann)
            if not self.is_connected:
                self.is_connected = True
                print('connecting')
                voice = await chann.connect()
                time.sleep(3)
                source = FFmpegPCMAudio('intro.mp3')
                player = voice.play(source)
                time.sleep(24)
                player = voice.stop()
        print(len(chann.members))

    def run(self):
        self.client.run(self.token)


def main():
    bot = Botty()
    bot.run()


if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        print(e)
