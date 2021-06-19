import discord
import os
from discord.ext import commands


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
        channel = after.channel
        bot_connection = member.guild.voice_client
        if str(member.nick) == "Test":
            if bot_connection:
                await bot_connection.move_to(channel)
            if not self.is_connected:
                self.is_connected = True
                print('connecting')
                await channel.connect()

        print(str(member.nick))

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
    # Simple bot that replies to hello messages.
    # Future methods will be added below
