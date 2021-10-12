import discord
from discord.ext import commands, tasks
import monitors
import os


class BotDS(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.pinger = monitors.Monitor(
            "Birth of the Demonic Sword",
            "https://www.webnovel.com/book/birth-of-the-demonic-sword_14187175405584205"
        )
        self.role = '<@&884991983943307265>'
        self.channelid = 884993117940486154
        self.looper.start()

    @tasks.loop(seconds=30.0)
    async def looper(self):
        if self.pinger.ping() and len(self.pinger.latestchapter) > 15:
            await self.bot.get_channel(self.channelid).send(
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
    async def statusbotds(self, ctx):
        await ctx.send(
            f"Role: {self.role}.\n Channel: <#{self.channelid}>.\n Latest: {self.pinger.latestchapter}"
        )

    @commands.command()
    async def triggerbotds(self, ctx):
        await self.bot.get_channel(self.channelid).send(
            f"Hey {self.role} **{self.pinger.name}** has released a new chapter ||{self.pinger.latestchapter[14:]}||"
        )


class CH(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.pinger = monitors.Monitor(
            "Chaos' Heir",
            "https://www.webnovel.com/book/chaos'-heir_20199782605918605")
        self.role = '<@&884992180459040798>'
        self.channelid = 884993117940486154
        self.looper.start()

    @tasks.loop(seconds=30.0)
    async def looper(self):
        if self.pinger.ping() and len(self.pinger.latestchapter) > 3:
            await self.bot.get_channel(self.channelid).send(
                f"Hey {self.role} **{self.pinger.name}** has released a new ||{self.pinger.latestchapter}||"
            )

    @looper.before_loop
    async def checks(self):
        if self.channelid is None:
            print("Hey <@556157454623309835>, Channel Id for CH is not set.")
        if self.role is None:
            print("Hey <@556157454623309835>, Role Id for CH is not set.")

    @commands.command()
    async def statusch(self, ctx):
        await ctx.send(
            f"Role: {self.role}.\n Channel: <#{self.channelid}>.\n Latest: {self.pinger.latestchapter}"
        )

    @commands.command()
    async def triggerch(self, ctx):
        await self.bot.get_channel(self.channelid).send(
            f"Hey {self.role} **{self.pinger.name}** has released a new ||{self.pinger.latestchapter}||"
        )


bot = commands.Bot(command_prefix=commands.when_mentioned_or(';~'))


@bot.event
async def on_ready():
    print(f'Logged in as {bot.user} (ID: {bot.user.id})')
    print('------')


TOKEN = os.environ["TOKEN"]

bot.add_cog(BotDS(bot))
bot.add_cog(CH(bot))

bot.run(TOKEN)
