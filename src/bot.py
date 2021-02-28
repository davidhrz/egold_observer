#!/usr/bin/python3
import discord
import answers
import utils
import graph
from discord.ext import tasks
from random import randint, random

# Only enable intents for server info and server messages
intents = discord.Intents(guilds=True, guild_messages=True)
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print('Logged in as {0.user}.'.format(client))
    refresh_presence.start()

@tasks.loop(seconds=30.0, count=None)
async def refresh_presence():
    value = round(randint(-25, 35) + random(), 2)
    message = f'eGLD: {value}$'
    activity = discord.Activity(name=message, type=discord.ActivityType.watching)
    await client.change_presence(status=discord.Status.online, activity=activity)

@client.event
async def on_message(message):
    # Ignore messages that don't summon the bot
    if message.author == client.user or (message.mentions != [client.user] and not message.content.startswith('obs$')):
        return

    # Ignore messages that contain a reference to another message
    if message.reference != None:
        return

    # Quote command
    if message.content.find('q') != -1:
        quote, author, (img_raw, img_ext) = answers.get_quote()
        while img_ext == None:
            print('Failed to get image extension. Getting new image...')
            quote, author, (img_raw, img_ext) = answers.get_quote()

        answer = f'*{quote}*\n- {author}'
        file = discord.File(img_raw, f'image.{img_ext}')
        await message.channel.send(content=answer, file=file)

    # Dev_refresh command
    elif message.content.find('dev_refresh') != -1:
        print('Refreshing data...')
        answers.refresh_data()
        print('Data refreshed.')

    # Graph command
    elif message.content.find('graph') != -1:
        answer = 'Graph over the last **1** day(s)'
        img_raw = graph.get_graph()

        file = discord.File(img_raw, f'image.png')
        await message.channel.send(content=answer, file=file)

    # Advice command
    else:
        answer, (img_raw, img_ext) = answers.get_advice()
        while img_ext == None:
            print('Failed to get image extension. Getting new image...')
            _, (img_raw, img_ext) = answers.get_advice()

        file = discord.File(img_raw, f'image.{img_ext}')
        await message.channel.send(content=answer, file=file)

answers.refresh_data()
client.run(utils.discord_token)
