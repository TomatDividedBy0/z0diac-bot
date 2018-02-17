import discord
from discord.ext import commands
import platform
import json
import os

with open('whoreppedwho.json','r') as f:
    f.close()
client = commands.Bot(command_prefix='!')
os.path.expanduser('./noboty')

# Startup Events


@client.event
async def on_ready():
    print('Logged in as '+client.user.name+' (ID:'+client.user.id+') | Connected to '+str(len(client.servers))+' servers | Connected to '+str(len(set(client.get_all_members())))+' users')
    print('--------')
    print('Current Discord.py Version: {} | Current Python Version: {}'.format(discord.__version__, platform.python_version()))

# Load a User's Reputation


@client.command(name='check', pass_context=True)
async def on_message(ctx):
    user_id = ctx.message.raw_mentions[0]
    os.chdir(r"C:\Users\fuzzy\PycharmProjects\noboty")
    json_file = open("dictionary.json", 'r')
    repkey = json.load(json_file)
    rep = repkey[user_id]
    await client.say(str(ctx.message.mentions[0])[:-5] + "'s" + ' ' + "reputation is" + ' ' + str(rep) + '.')

# Adding Voting To Messages


@client.command(name = 'poll', pass_context=True)
async def poll(ctx):
    await client.add_reaction(ctx.message,'👍')
    await client.add_reaction(ctx.message,'👎')

# Adds Reputation Dicts for New Users


@client.event
async def on_member_join(user):
    rep_dict = {user.id: 0}
    with open('dictionary.json') as f:
        key = json.load(f)
    key.update(rep_dict)
    with open('dictionary.json', 'w') as f:
        json.dump(key, f)

# Allows Users To Change Reputation


@client.command(name='repup', pass_context=True)
async def repup(ctx):
    # Adds tag to show who repped who
    with open('whoreppedwho.json','r') as f:
        positive_id = str(int(ctx.message.raw_mentions[0]))
        whoreppedwho_dict = ctx.message.author.id + positive_id
        whoreppedwho_dict2 = '-' + ctx.message.author.id + positive_id
        who_rep = json.load(f)
        enoughwiththevariables = who_rep[whoreppedwho_dict]
        try:
            enoughwiththevariables = who_rep[whoreppedwho_dict]
        except KeyError:
            with open('dictionary.json', 'w') as f:
                rep_calibrate = json.load(f)
                rep_calibrate2= rep_calibrate[str(int(ctx.message.raw_mentions[0]))]
                repcalibrate3 = {str(int(ctx.message.raw_mentions[0])): rep_calibrate2}
                rep_calibrate.update(repcalibrate3)
                f.seek(0)
                json.dump(rep_calibrate, f)
        print(enoughwiththevariables)
        f.close()
        if who_rep[whoreppedwho_dict] is False:
            await client.say("You have already uprepped this user!")
        else:
            with open('whoreppedwho.json', 'w') as f:
                repwho = {whoreppedwho_dict: False}
                who_rep.update(repwho)
                print(who_rep[whoreppedwho_dict])
                json.dump(who_rep, f)
            user_id = ctx.message.raw_mentions[0]
            if who_rep[whoreppedwho_dict2] is False:
                with open('dictionary.json', 'r+') as f:
                    repkey = json.load(f)
                    repkey[user_id] = (int(repkey[user_id]) - 2)
                    f.seek(0)
                    json.dump(repkey, f)
                    f.truncate()
            else:
                with open('dictionary.json', 'r+') as f:
                    repkey = json.load(f)
                    repkey[user_id] = (int(repkey[user_id]) - 1)
                    f.seek(0)
                    json.dump(repkey, f)
                    f.truncate()
            await client.say('You have successfully uprepped ' + str(ctx.message.mentions[0])[:-5] + ".")


@client.command(name='repdown', pass_context=True)
async def repdown(ctx):
    # Adds tag to show who repped who
    with open('whoreppedwho.json','r') as f:
        negative_id = str(int(ctx.message.raw_mentions[0]))
        whoreppedwho_dict = '-' + ctx.message.author.id + negative_id
        whoreppedwho_dict2 = ctx.message.author.id + negative_id
        who_rep = json.load(f)
        try:
            enoughwiththevariables = who_rep[whoreppedwho_dict]
        except KeyError:
            with open('dictionary.json', 'r') as f:
                rep_calibrate = json.load(f)
            with open('dictionary.json', 'w') as f:
                rep_calibrate2= rep_calibrate[str(int(ctx.message.raw_mentions[0]))]
                repcalibrate3 = {str(int(ctx.message.raw_mentions[0])): rep_calibrate2}
                rep_calibrate.update(repcalibrate3)
                f.seek(0)
                json.dump(rep_calibrate, f)
            if who_rep[whoreppedwho_dict2] is False:
                await client.say("You have already downrepped this user!")
            else:
                with open('whoreppedwho.json', 'w') as f:
                    repwho = {whoreppedwho_dict2: False}
                    who_rep.update(repwho)
                    print(who_rep[whoreppedwho_dict])
                    json.dump(who_rep, f)
                user_id = ctx.message.raw_mentions[0]
                if who_rep[whoreppedwho_dict2] is False:
                    with open('dictionary.json', 'r+') as f:
                        repkey = json.load(f)
                        repkey[user_id] = (int(repkey[user_id]) - 2)
                        f.seek(0)
                        json.dump(repkey, f)
                        f.truncate()
                else:
                    with open('dictionary.json', 'r+') as f:
                        repkey = json.load(f)
                        repkey[user_id] = (int(repkey[user_id]) - 1)
                        f.seek(0)
                        json.dump(repkey, f)
                        f.truncate()
                await client.say('You have successfully downrepped ' + str(ctx.message.mentions[0])[:-5] + ".")


@client.command(name='repregister',pass_context=True)
async def repregister(ctx):
    rep_dict = {ctx.message.author.id: 0}
    with open('dictionary.json') as f:
        key = json.load(f)
    key.update(rep_dict)
    with open('dictionary.json', 'w') as f:
        json.dump(key, f)
    client.say((str(ctx.message.author))[:-5] + ' has been successfully registered.')


@client.command(name='selfaware')
async def selfaware():
    await client.say('!repregister')


client.run('MzgzMzg1MTk4NTM0MDY2MTg3.DUe7Ug.rJrJfliabqp3a_TGUIVKKqkvlgw')
