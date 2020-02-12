#coding:UTF-8
import discord
from discord.ext import tasks

# 自分のBotのアクセストークンに置き換えてください
TOKEN = 'Njc2NzcwNjY3NjUxMzk5NzEx.XkQwCA.6GXGif45hWZ7PA0HR9hzaphsyRk'
CHANNEL_ID = 676772811595055136

# 接続に必要なオブジェクトを生成
client = discord.Client()

# 60秒に一回ループ
@tasks.loop(seconds=5)
async def loop():
    channel = client.get_channel(CHANNEL_ID)
    await channel.send('5秒たったよ')  

#ループ処理実行
loop.start()

# Botの起動とDiscordサーバーへの接続
client.run(TOKEN)
