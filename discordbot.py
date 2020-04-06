import discord
from discord.ext import tasks
from datetime import datetime

import os

client = discord.Client()

token = os.environ['DISCORD_BOT_TOKEN']

@tasks.loop(seconds=60)
async def loop():
    now = datetime.now().strftime('%m/%d-%H:%M')
    if now == '04/06-22:42':
        alert_channel = client.get_channel(694093239954833412)
        msg = f'DSS説明会まであと15分！'
        await alert_channel.send(msg)

loop.start()

client.run(token)
