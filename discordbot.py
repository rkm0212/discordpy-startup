from discord.ext import commands
import os
import traceback

bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']


@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)

@client.event
async def on_ready():
    CHANNEL_ID = 676772811595055136 # 任意のチャンネルID(int)
    channel = client.get_channel(CHANNEL_ID)
    await channel.send('おはよう！')


@bot.command()
async def ping(ctx):
    await ctx.send('norplellll')


bot.run(token)
