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
    message1 = await z0diac.get_channel(451557947194212362).get_message(451558090727358495)
    await message1.add_reaction(z0diac.get_emoji(448479894725459968))
    await message1.add_reaction(z0diac.get_emoji(448479501018464256))
    await message1.add_reaction(z0diac.get_emoji(448479331220455434))
    await message1.add_reaction(z0diac.get_emoji(448479686511689728))
    await message1.add_reaction(z0diac.get_emoji(448636465417814026))
    message2 = await z0diac.get_channel(451557947194212362).get_message(451558008787566593)
    await message2.add_reaction(z0diac.get_emoji(448475108290592769))
    await message2.add_reaction(z0diac.get_emoji(448477016430215169))
    await message2.add_reaction(z0diac.get_emoji(448477539233431563))
    await message2.add_reaction(z0diac.get_emoji(448477746138578944))
    message3 = await z0diac.get_channel(451557947194212362).get_message(451558134784196611)
    await message3.add_reaction(z0diac.get_emoji(448478006747332608))
    await message3.add_reaction(z0diac.get_emoji(448478811076427786))
    await message3.add_reaction(z0diac.get_emoji(448478542444101643))
    await message3.add_reaction(z0diac.get_emoji(448478811076427786))
    await message3.add_reaction(z0diac.get_emoji(448478976252444673))
    await message3.add_reaction(z0diac.get_emoji(448478321743888406))
    message4 = await z0diac.get_channel(451557947194212362).get_message(451558174965760000)
    await message4.add_reaction(z0diac.get_emoji(448485954462679060))


z0diac.run("MzgzMzg1MTk4NTM0MDY2MTg3.DeSjjg.UTV6BKxXzMrqIVmgMDahKsfZDzs")