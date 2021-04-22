#!/bin/python3
import os
import discord
import json
import functions

client = discord.Client()

@client.event
async def on_ready():
    for guild in client.guilds:
        if guild.name == os.getenv('DISCORD_SERVER'):
            break

        print(
            f'{client.user} is connected to the following guild:\n'
            f'{guild.name}(id: {guild.id})'
        )

# This is where you put the commabds
@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$dave'):
        # Caution, Profanity
        msg = "Fuck you, Dave"
        await message.channel.send(msg)

    if message.content.startswith('$birthday'):
        birthday_control(msg)

functions.bot_init()
client.run(os.getenv('DISCORD_TOKEN'))