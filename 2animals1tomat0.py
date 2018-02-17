import discord
from discord.ext import commands
import platform
import json
import os

client = commands.Bot(command_prefix='!')
os.path.expanduser('./noboty')


@client.command(name='specs')
async def specs():
    await client.say('**CPU:** Opteron 1389\n**GPU:** Radeon R7 360\n**HDD:** 1TB HDD\n**RAM:** 8GB DDR3')


@client.event
async def on_member_join(user):
    rep_dict = {user.id: 0}
    with open('dictionary.json') as f:
        key = json.load(f)
    key.update(rep_dict)
    with open('dictionary.json', 'w') as f:
        json.dump(key, f)


client.run('MzgzMzg1MTk4NTM0MDY2MTg3.DUwMaQ.wj3irl5hL_d1Nt_D2ZfWX6j5xYE')