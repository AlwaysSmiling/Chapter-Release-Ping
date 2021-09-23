import discord
from discord.ext import commands, tasks
import monitors
import os
#from keep_alive import keep_alive
#from replit import db               #currently hosted in replit so using replit database.

#TOKEN = os.environ['bot_token']
'''
this is an example for declaring stuff for the preformatted message

botds = "**Birth of the Demonic Sword**"
ch = "**Chaos' Heir**"
upchan = #channel-id
admins = '<@&role-id>'
botdsrole = '<@&role-id>'
chrole = '<@&role-id>'
'''

#class MyClient(discord.Client):
#    def __init__(self, *args, **kwargs):
#        super().__init__(*args, **kwargs)
#
#        self.BotDSping = monitors.MonitorBotDS()
#        self.CHping = monitors.MonitorCH()
#        self.my_background_task.start()
#
#    async def on_ready(self):
#        print(f'Logged in as {self.user} (ID: {self.user.id})')
#        print('------')
#
#    @tasks.loop(seconds=30) # task runs every 60 seconds
#    async def my_background_task(self):
#        if self.BotDSping.ping():
#            await self.get_channel(upchan).send(f"Hey {botdsrole} {botds} has released a new chapter ||{db['botds'][14:]}||")
#        if self.CHping.ping():
#            await self.get_channel(upchan).send(f"Hey {chrole} {ch} has released a new ||{db['ch']}||")
#
#    @my_background_task.before_loop
#    async def before_my_task(self):
#        self.BotDSping.ping()
#        self.CHping.ping()
#        print(db['botds'], db['ch'])
#        await self.wait_until_ready() # wait until the bot logs in
#
#    async def on_message(self, message):
#        if message.author == self.user:
#            return
#
#        if message.author.id == 'member.id' and 'trigger botds' in message.content: #manual trigger
#            await self.get_channel('channel-id').send(f"Hey  {botds} has released a new chapter ||{db['botds'][14:]}||")
#
#        if message.author.id == 'member-id' and 'trigger ch' in message.content:  #manual trigger
#            await self.get_channel(upchan).send(f"Hey {chrole} {ch} has released a new ||{db['ch']}||")
#
#        if 'sr! hi' in message.content and message.author.id == 'member-id':
#            await message.channel.send('Hello!')

#client = MyClient()
#keep_alive()
#client.run(TOKEN)


class BotDS(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.pinger = monitors.Monitor(
            "Birth of the Demonic Sword",
            "https://www.webnovel.com/book/birth-of-the-demonic-sword_14187175405584205"
        )
        self.role = None
        self.channelid = None

    @tasks.loop(seconds=30.0)
    async def looper(self):
        if self.pinger.ping() and len(self.pinger.latestchapter) > 15:
            await self.get_channel(self.channelid).send(
                f"Hey {self.role} **{self.pinger.name}** has released a new chapter ||{self.pinger.latestchapter[14:]}||"
            )

    @looper.before_loop
    async def checks(self):
        if self.channelid is None:
            await self.get_channel(889410354155753486).send(
                "Hey <@556157454623309835>, Channel Id for BotDS is not set.")
        if self.role is None:
            await self.get_channel(889410354155753486).send(
                "Hey <@556157454623309835>, Role Id for BotDS is not set.")

    @commands.command()
    async def startbotdslooper(self, ctx):
        try:
            self.looper.start()
            await ctx.send("successfully started loop")
        except:
            await ctx.send("yea, somebody somewhere fucked up")

    @commands.command()
    async def stopbotdslooper(self, ctx):
        try:
            self.looper.cancel()
            await ctx.send("successfully stopped loop")
        except:
            await ctx.send("yea, somebody somewhere fucked up")

    @commands.command()
    async def setbotdsrole(self, ctx, id):
        try:
            self.role = f'<@{id}>'
            ctx.send("Role Id Set successfully.")
        except:
            ctx.send("failed..... T_T ")

    @commands.command()
    async def setbotdschannelid(self, ctx, channelid: int):
        try:
            self.channelid = channelid
            ctx.send("Channel Id Set successfully.")
        except:
            ctx.send("failed..... T_T ")


class CH(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.pinger = monitors.Monitor(
            "Chaos' Heir",
            "https://www.webnovel.com/book/chaos'-heir_20199782605918605")
        self.role = None
        self.channelid = None

    @tasks.loop(seconds=30.0)
    async def looper(self):
        if self.pinger.ping() and len(self.pinger.latestchapter) > 3:
            await self.get_channel(self.channelid).send(
                f"Hey {self.role} **{self.pinger.name}** has released a new ||{self.pinger.latestchapter}||"
            )

    @looper.before_loop
    async def checks(self):
        if self.channelid is None:
            await self.get_channel(889410354155753486).send(
                "Hey <@556157454623309835>, Channel Id for CH is not set.")
        if self.role is None:
            await self.get_channel(889410354155753486).send(
                "Hey <@556157454623309835>, Role Id for CH is not set.")

    @commands.command()
    async def startchlooper(self, ctx):
        try:
            self.looper.start()
            await ctx.send("successfully started loop")
        except:
            await ctx.send("yea, somebody somewhere fucked up")

    @commands.command()
    async def stopchlooper(self, ctx):
        try:
            self.looper.cancel()
            await ctx.send("successfully stopped loop")
        except:
            await ctx.send("yea, somebody somewhere fucked up")

    @commands.command()
    async def setchrole(self, ctx, id: str):
        try:
            self.role = f'<@{id}>'
            ctx.send("Role Id Set successfully.")
        except:
            ctx.send("failed..... T_T ")

    @commands.command()
    async def setchchannelid(self, ctx, channelid: int):
        try:
            self.channelid = channelid
            ctx.send("Channel Id Set successfully.")
        except:
            ctx.send("failed..... T_T ")


bot = commands.Bot(command_prefix=commands.when_mentioned_or(';~'))


@bot.event
async def on_ready():
    print(f'Logged in as {bot.user} (ID: {bot.user.id})')
    print('------')


TOKEN = "Nzk0MTk2ODA1NTkxMjM2NjE4.X-3TaQ.sIY2fIfYOdsJMTWMUTadid3bzD8"

bot.add_cog(BotDS)
bot.add_cog(CH)
bot.run(TOKEN)
