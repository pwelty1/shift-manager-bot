# bot.py
import os
import discord
from discord.ext import tasks, commands
from dotenv import load_dotenv
import datetime


load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
members = {}
client = discord.Client()
text_channel_id = ''

@client.event
async def on_ready():

    @tasks.loop(seconds=30) #hours=24
    async def send_message():
        if datetime.datetime.today().weekday() >= 0 and datetime.datetime.today().weekday() < 5: 
            channel = client.get_channel(text_channel_id)
            if datetime.datetime.today().weekday() == 0:
                file = discord.File("Monday.png")
                in_person = 'In-Office Rotation:\n '
            elif datetime.datetime.today().weekday() == 1:
                file = discord.File("Tuesday.png")
            elif datetime.datetime.today().weekday() == 2:
                file = discord.File("Wednesday.png")
            elif datetime.datetime.today().weekday() == 3:
                file = discord.File("Thursday.png")
                in_person = '\nIn-Office Rotation:\n @pwelty#5941 '
            elif datetime.datetime.today().weekday() == 4:
                file = discord.File("Friday.png")
            
            await channel.send(file=file, content="Today's Shifts @everyone")
            await channel.send(in_person)
        
        # await channel.send('I am a broken record')

    print(f'{client.user} has connected to Discord!')
    for server in client.guilds:
        for channel in server.channels:
            if channel.name == 'general':
                text_channel_id = channel.id
    channel = client.get_channel(text_channel_id)

    for server in client.guilds:
        for member in server.members:
            print(member)

    await channel.send('Ready to problem solve!')
    send_message.start()



client.run(TOKEN)