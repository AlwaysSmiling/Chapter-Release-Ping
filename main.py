import discord
from discord.ext import commands, tasks
import monitors
import os
from keep_alive import keep_alive
from replit import db               #currently hosted in replit so using replit database.

TOKEN = os.environ['bot_token']
'''
this is an example for declaring stuff for the preformatted message

botds = "**Birth of the Demonic Sword**"
ch = "**Chaos' Heir**"
upchan = #channel-id
admins = '<@&role-id>'
botdsrole = '<@&role-id>'
chrole = '<@&role-id>'
'''

class MyClient(discord.Client):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.BotDSping = monitors.MonitorBotDS()
        self.CHping = monitors.MonitorCH()
        self.my_background_task.start()

    async def on_ready(self):
        print(f'Logged in as {self.user} (ID: {self.user.id})')
        print('------')

    @tasks.loop(seconds=30) # task runs every 60 seconds
    async def my_background_task(self):
        if self.BotDSping.ping():
            await self.get_channel(upchan).send(f"Hey {botdsrole} {botds} has released a new chapter ||{db['botds'][14:]}||")
        if self.CHping.ping():
            await self.get_channel(upchan).send(f"Hey {chrole} {ch} has released a new ||{db['ch']}||")

    @my_background_task.before_loop
    async def before_my_task(self):
        self.BotDSping.ping()
        self.CHping.ping()
        print(db['botds'], db['ch'])
        await self.wait_until_ready() # wait until the bot logs in

    async def on_message(self, message):
        if message.author == self.user:
            return

        if message.author.id == 'member.id' and 'trigger botds' in message.content: #manual trigger
            await self.get_channel('channel-id').send(f"Hey  {botds} has released a new chapter ||{db['botds'][14:]}||")

        if message.author.id == 'member-id' and 'trigger ch' in message.content:  #manual trigger
            await self.get_channel(upchan).send(f"Hey {chrole} {ch} has released a new ||{db['ch']}||")            

        if 'sr! hi' in message.content and message.author.id == 'member-id':
            await message.channel.send('Hello!')

client = MyClient()
keep_alive()
client.run(TOKEN)
