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
    with open('whoreppedwho.json','r+') as f:
        positive_id = str(ctx.message.raw_mentions[0])
        whoreppedwho_dict = ctx.message.author.id + positive_id
        whoreppedwho_dict2 = '-' + ctx.message.author.id + positive_id
        who_rep = json.load(f)
        try:
            enoughwiththevariables = who_rep[whoreppedwho_dict]
        except KeyError:
            with open('dictionary.json', 'r+') as f:
                rep_calibrate = json.load(f)
                rep_calibrate2= rep_calibrate[str(int(ctx.message.raw_mentions[0]))]
                repcalibrate3 = {str(int(ctx.message.raw_mentions[0])): rep_calibrate2}
                rep_calibrate.update(repcalibrate3)
                f.seek(0)
                f.truncate()
                json.dump(json.load(f), f)
        print(enoughwiththevariables)
        f.close()
        try:
            if who_rep[whoreppedwho_dict] is 0:
                await client.say("You have already uprepped this user!")
            else:
                with open('whoreppedwho.json', 'r+') as f:
                    repwho = {whoreppedwho_dict: 0}
                    who_rep.update(repwho)
                    print(who_rep[whoreppedwho_dict])
                    f.seek(0)
                    f.truncate()
                    json.dump(who_rep, f)
                user_id = ctx.message.raw_mentions[0]
                if who_rep[whoreppedwho_dict2] is -1:
                    with open('dictionary.json', 'r+') as f:
                        repkey = json.load(f)
                        repkey1andhalf = repkey[(str(ctx.message.raw_mentions[0]))].key
                        repkey2 = {repkey: (int(repkey1andhalf) + 2)}
                        repkey.update(repkey2)
                        f.seek(0)
                        f.truncate()
                        json.dump(repkey, f)
                else:
                    with open('dictionary.json', 'r+') as f:
                        repkey = json.load(f)
                        repkey1andhalf = repkey[user_id].key
                        repkey2 = {repkey: (int(repkey1andhalf) + 1)}
                        repkey.update(repkey2)
                        json.dump(repkey, f)
                    with open('whoreppedwho.json', 'r+') as f:
                        status = {whoreppedwho_dict2: True}
                        whoreppedwho_dict2.update(status)
                        f.seek(0)
                        f.truncate()
                        json.dump(whoreppedwho_dict2, f)
                await client.say('You have successfully uprepped ' + str(ctx.message.mentions[0])[:-5] + ".")
        except KeyError:
            with open('whoreppedwho.json', 'r') as f:
                whoreppedwho_calibrate = json.load(f)
            with open('whoreppedwho.json', 'w') as f:
                whoreppedwho_calibrate3 = {whoreppedwho_dict: True}
                whoreppedwho_calibrate.update(whoreppedwho_calibrate3)
                f.seek(0)
                json.dump(whoreppedwho_calibrate, f)


@client.command(name='repdown', pass_context=True)
async def repdown(ctx):
    # Adds tag to show who repped who
    with open('whoreppedwho.json','r') as f:
        negative_id = str(ctx.message.raw_mentions[0])
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
        try:
            if who_rep[whoreppedwho_dict] is 0:
                await client.say("You have already downrepped this user!")
            else:
                with open('whoreppedwho.json', 'r') as f:
                    repwho = {whoreppedwho_dict: 0}
                    who_rep.update(repwho)
                    print(who_rep[whoreppedwho_dict])
                    f.seek(0)
                    f.truncate()
                    json.dump(who_rep, f)
                user_id = str(ctx.message.raw_mentions[0])
                if who_rep[whoreppedwho_dict2] is 1:
                    with open('dictionary.json', 'r+') as f:
                        repkey = json.load(f)
                        repkey1andhalf = repkey[str(ctx.message.raw_mentions[0])].key
                        repkey2 = {repkey: (int(repkey1andhalf) - 2)}
                        repkey.update(repkey2)
                        json.dump(repkey, f)
                    with open('whoreppedwho.json', 'r+') as f:
                        status = {whoreppedwho_dict2: -2}
                        whoreppedwho_dict2.update(status)
                        f.seek(0)
                        f.truncate()
                        json.dump(whoreppedwho_dict2, f)
                else:
                    with open('dictionary.json', 'r+') as f:
                        repkey = json.load(f)
                        repkey1andhalf = repkey[user_id].key
                        repkey2 = {repkey: (int(repkey1andhalf) + 1)}
                        repkey.update(repkey2)
                        json.dump(repkey, f)
                await client.say('You have successfully downrepped ' + str(ctx.message.mentions[0])[:-5] + ".")
        except KeyError:
            with open('whoreppedwho.json', 'r') as f:
                whoreppedwho_calibrate = json.load(f)
            with open('whoreppedwho.json', 'r+') as f:
                whoreppedwho_calibrate3 = {whoreppedwho_dict: -1}
                whoreppedwho_calibrate.update(whoreppedwho_calibrate3)
                f.seek(0)
                json.dump(whoreppedwho_calibrate, f)


@client.command(name='role', pass_context=True)
async def role(ctx):
    role_list = ["Classical Liberal", "Blue Dog", "Social Democrat", "Left Libertarian", "Neoconservative", "Neoliberal", "Socialist", "Paleoconservative", "Nationalist" , "Evangelical" , "Right Libertarian" , "Centrist"]
    print(ctx.message.content[6:])
    if ctx.message.content[6:] in role_list:
        roleo = discord.utils.get(ctx.message.server.roles, name=ctx.message.content[6:])
        await client.add_roles(ctx.message.author,roleo)
        await client.say("You are now added as a " + ctx.message.content[6:] + "!")
    else:
        await client.say("That is not a role, refer to #welcome for a list of roles.")


@client.command(name='subrole', pass_context=True)
async def subrole(ctx):
    print(ctx.message.content[9:])
    await client.create_role(ctx.message.author.server, name = ctx.message.content[9:])
    roleo = discord.utils.get(ctx.message.server.roles, name=ctx.message.content[9:])
    await client.add_roles(ctx.message.author,roleo)
    await client.say("Your subrole has been added.")


@client.command(name='pronoun', pass_context=True)
async def pronoun(ctx):
    print(ctx.message.content[9:])
    await client.create_role(ctx.message.author.server, name=ctx.message.content[9:])
    roleo = discord.utils.get(ctx.message.server.roles, name=ctx.message.content[9:])
    await client.add_roles(ctx.message.author,roleo)
    await client.say("Your pronoun has been added.")


@client.event
async def on_message(message):
    if message.author is message.server.get_member('173451290268008448'):
        print('Success')
        await client.add_reaction(message,'⭐')
    else:
        print('Failed')


@client.event
async def on_member_join(user):
    await client.send_message(client.get_channel('381184797495787530'), str(user.mention + " , please register your role with our bot using `!role [your role]`. Check #welcome for a list of roles."))


@client.command(name='repregister_everyone',pass_context=True)
async def repregister_everyone(ctx):
    rep_dict0 = client.get_server('381170494814289922')
    rep_dict1 = client.get_server('400640134548029453')
    rep_dict2 = client.get_server('176160569798295554')
    rep_dict3 = client.get_server('406536119182819329')
    rep_dict = [{members.id: 0} for members in (list(rep_dict0.members) + list(rep_dict1.members) + list(rep_dict2.members) + list(rep_dict3.members))]
    print(rep_dict)
    with open('dictionary.json') as f:
        key = json.load(f)
    with open('dictionary.json', 'w') as f:
        json.dump(rep_dict, f)


@client.command(name='specs')
async def specs():
    await client.say('**CPU:** Opteron 1389\n**GPU:** Radeon R7 360\n**HDD:** 1TB HDD\n**RAM:** 8GB DDR3')


client.run('XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX')

