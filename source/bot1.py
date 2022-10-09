import discord
import csv
import time_reader
import data_maker2
from discord.ext import tasks

'''
made by climentia
Created in 2022
Rights reserved by @climentia
'''


intents = discord.Intents.default()  # デフォルトのIntentsオブジェクトを生成
intents.typing = False  # typingを受け取らないように
client = discord.Client(intents=intents)

with open('../token.txt') as f:
    reader = csv.reader(f)
    for row in reader:
        TOKEN = row[1]

"""@client.event
async def on_message(message):
    #bot自身が送信したメッセージには反応しない
    if message.author == client.user:
        return
    if message.content.startswith('朝潮ちゃんの'):
        await message.channel.send('ネコミミ')"""

channel_sent = None
@tasks.loop(seconds=60)
async def send_message_every_60sec():
    sleepTime = 0
    # 現在の時刻
    tr = time_reader.TimeReader()
    dt = tr.get_time()
    # 指定時間のとき
    if (dt.weekday() == 6) and (dt.hour == 16) and (dt.minute == 10):
        # channel = client.get_channel(CHANNEL_ID)
        dm = data_maker2.DataMaker()
        dm_a = dm.stock_year_figure_maker()
        dm_m = dm.stock_month_figure_maker()
        await channel_sent.send(str(dt.month) + "月" +str(dt.day) + "日の株価情報です。\nMonthly chart", file=discord.File("Monthly stock price change.png"))
        await channel_sent.send("Annual chart", file=discord.File("Annual stock price change.png"))


@client.event
async def on_ready():
    global channel_sent 
    channel_sent = client.get_channel(1026088708107153430)
    send_message_every_60sec.start()

client.run(TOKEN)