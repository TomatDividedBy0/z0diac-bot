import discord
from discord.ext import commands
import time
import json
import traceback
from PyDictionary import PyDictionary

dictionary=PyDictionary()


z0diac = commands.Bot(command_prefix= '/', description='A bot for the Political Watering Hole.')


@z0diac.event
async def on_ready():
    print('Connected to '+str(len(set(z0diac.get_all_members())))+' users')
    print('--------')


@z0diac.command()
async def archive(ctx):
    if ctx.message.author == z0diac.get_member(176160436331216896):
         async with ctx.typing():
                y = await z0diac.get_channel(432574353822056448).pins()
                y.reverse()
                for x in y:
                    try:
                        embed = discord.Embed(title=(x.author.display_name + " (" + x.created_at.strftime("%Y-%m-%d %H:%M:%S") + ")"), color=x.author.color, description=x.content)
                        embed.set_thumbnail(url=x.author.avatar_url)
                        await z0diac.get_channel(446400765775314947).send(embed=embed)
                    except:
                        embed = discord.Embed(title=(x.author.display_name + " (" + x.created_at.strftime("%Y-%m-%d %H:%M:%S") + ")"),description=x.content)
                        embed.set_thumbnail(url=x.author.avatar_url)
                        await z0diac.get_channel(446400765775314947).send(embed=embed)
    else:
        await ctx.channel.send("You do not have permission to use this.")


@z0diac.command()
async def getunicode(ctx):
    print(ctx.message.content)
    message3 = await z0diac.get_channel(451557947194212362).get_message(451558090727358495)
    await message3.add_reaction(z0diac.get_emoji(454665209009668097))
    await message3.add_reaction(z0diac.get_emoji(454664092305588235))
    await message3.add_reaction(z0diac.get_emoji(454666880771424258))
    await message3.add_reaction(z0diac.get_emoji(454666611568410634))
    await message3.add_reaction(z0diac.get_emoji(454664747464392724))
    message2 = await z0diac.get_channel(451557947194212362).get_message(451558008787566593)
    await message2.add_reaction(z0diac.get_emoji(454664511173951494))
    await message2.add_reaction(z0diac.get_emoji(454666536142110721))
    await message2.add_reaction(z0diac.get_emoji(454666012860743695))
    await message2.add_reaction(z0diac.get_emoji(454663573386559499))
    message1 = await z0diac.get_channel(451557947194212362).get_message(451558134784196611)
    await message1.add_reaction(z0diac.get_emoji(454667115601854474))
    await message1.add_reaction(z0diac.get_emoji(454663251633111050))
    await message1.add_reaction(z0diac.get_emoji(454665463847321602))
    await message1.add_reaction(z0diac.get_emoji(454663855809757195))
    await message1.add_reaction(z0diac.get_emoji(454662578488999937))
    message4 = await z0diac.get_channel(451557947194212362).get_message(451558174965760000)
    await message4.add_reaction(z0diac.get_emoji(448485954462679060))


z0diac.run("MzgzMzg1MTk4NTM0MDY2MTg3.DeSjjg.UTV6BKxXzMrqIVmgMDahKsfZDzs")