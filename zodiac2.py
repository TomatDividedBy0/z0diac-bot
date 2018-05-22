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



# Adding Voting To Messages



@z0diac.command()
async def poll(ctx):
    await ctx.message.add_reaction('👍')
    await ctx.message.add_reaction('👎')


@z0diac.command()
async def whatis(ctx):
    label = ctx.message.content[8:]
    if ctx.channel != z0diac.get_channel(432574353822056448):
        if label == "Socialist" or label == "socialist" or label == "Socialists" or label == "socialists":
            await ctx.channel.send("Socialists believe in the public ownership of the means of production. They are commonly found on the far-left end of the compass, with varying degrees of authoritarianism/libertarianism.")
        elif label == "Classical Liberal" or label == "classical liberal" or label == "classical lib" or label == "Classical liberal" or label == "Classical Lib" or label == "Classical lib":
            await ctx.message.channel.send("Classical liberals adhere strongly to the rights of the individual, however, unlike libertarians, they are a lot more moderate on the free market. You'll usually find them straight down from center or near center.")
        elif label == "Nationalist" or label == "nationalist":
            await ctx.message.channel.send("Nationalists believe in putting their own country or group first above others. They are often protectionist, and come in many different variants from Civic Nationalists to NazBols to Ethnonationalists.")
        elif label == "Right Libertarian" or label == "Libertarian" or label == "libertarian" or label == "right libertarian":
            await ctx.message.channel.send("Libertarians tend to favor solutions that involve the free market and the individual over government intervention, detesting excess public spending and tax hikes. They are found everywhere on the bottom right of the compass.")
        elif label == "Paleoconservative" or label == "paleocon" or label == "paleoconservative" or label == "paleocon":
            await ctx.channel.send("Paleoconservatives, also known as the Old Right, date back to the early 20th century in their beliefs. They place social tradition and economic nonintervention above all else, often being in the top right of the compass.")
        elif label == "LibtSoc" or label == "Libertarian Socialist" or label == "Libertarian Socialist" or label == "libertarian socialist":
            await ctx.channel.send(" Libertarian Socialists/AnComs advocate for the abolition of state and private property as a means to liberate people.")
        elif label == "SocDem" or label == "socdem" or label == "social democrat" or label == "Social Democrat" or label == "Social democrat" or label == "Socdem":
            await ctx.channel.send("Social Democrats believe in using government as a tool to bring about social progress and change. They lean authoritative, intersect with social justice, and are typically found on the left.")
        elif label == "green" or label == "Green" or label == "left libertarian":
            await ctx.channel.send("Greens tend to be less about the economic liberty and more about the social and infrastructure liberty, especially on envrionmental issues. The open source community and net neutrality opponents are good examples of Greens.")
        elif label == "Neoliberal" or label == "neolib" or label == "neoliberal":
            await ctx.channel.send("Neoliberalism mixes aspects of progressivism and classical liberalism to create an ideology that's moderate, pragmatic, and often focused on values such as globalism, lower government spending, and deregulation.")
        elif label == "centrist" or label == "Centrist":
            await ctx.channel.send("Centrists don't particularly lean any noticeable amount on the left/right scale; their policies are often moderate, and they focus on compromise over ideological passion. They can be anywhere on the authoritarian/libertarian scale.")
        elif label == "neocon" or label == "neoconservative" or label == "Neoconservative" or label == "Neocon":
            await ctx.channel.send("Neoconservatism is a foreign policy theory that builds on the idea that it's a democratic country's duty to spread its values through foreign intervention. On most issues but foreign policy, they tend to be more moderate.")
        elif label == "Paternalist" or label  == "paternalist":
            await ctx.channel.send("Paternalists believe in the state taking a parent role, being authoritative on social policy, but interventionist economically.")
        elif label == "Paleoliberal" or label == "Paleolib" or label == "paleoliberal" or label == "paleolib":
            await ctx.channel.send("A paleoliberal or a RINO/Whig in the US is a term for a conservative who is a lot more moderate and centrist in their beliefs. They typically are found close to the center on issues of tradition, being economically to the right, typically being the parallel to Blue Dogs.")
        elif label == "Theologue" or label == "theologue":
            await ctx.channel.send("Theologues are socially conservative, but vary widely on their economic policies. This includes Distributists, Christian Democrats, and right-theologues. Their main deciding factor in voting is their religion.")
        elif label == "On Sale" or label == "for sale" or label == "For sale" or label == "forsale" or label == "Forsale" or label == "forSale":
            await ctx.channel.send("Currently, we have the following items:\n -ad\n -renamefuco\n -membership\n -bigdab\n -subrole.\n Do `/whatis [Item]` to learn about pricing and descriptions.")
        elif label == "specs" or label == "Specs" or label == "yourspecs" or label== "your specs":
            await ctx.channel.send('**CPU:** Opteron 3365\n**GPU:** Radeon R7 360\n**HDD:** 320GB HDD\n**RAM:** 8GB DDR3\n**OS:** Kubuntu')
        elif label == "myBalance" or label == "mybalance" or label == "my balance":
            with open("dictionary.json", 'r') as f:
                repkey = json.load(f)
                await ctx.send(str(ctx.message.author.name) + " has " + str(repkey.get(str(ctx.message.author.id))) + ' Effort Points.')
        elif label == "myideology" or label == "my ideology" or label == "myIdeology":
            await ctx.message.delete()
            message_to = await ctx.message.author.send("Welcome to the official compact edition of the PWH political test. \nYou will be asked various questions on your values to determine your ideology. You will be presented with multiple choices ranging from A to E. Simply click the corresponding button to answer said question. To begin, click the green check mark.")
            await message_to.add_reaction('✅')
            def check(reaction, user):
                return reaction.count == 2
            await z0diac.wait_for('reaction_add',check=check)
            message_3 = await ctx.message.author.send("**Question 1:**\nDo you support the existence of a government? (Y for yes, and N for no.)")
            await message_3.add_reaction('🇾')
            await message_3.add_reaction('🇳')
            def check(reaction, user):
                return reaction.count == 2
            reaction2 = await z0diac.wait_for('reaction_add', check=check)
            if reaction2[0].emoji == '🇾':
                message = await ctx.message.author.send("**Question 2:**\nDo you believe said government should be in charge of the market? (Y for yes, and N for no.)")
                await message.add_reaction('🇾')
                await message.add_reaction('🇳')
                def check(reaction, user):
                    return reaction.count == 2
                reaction2 = await z0diac.wait_for('reaction_add', check=check)
                if reaction2[0].emoji == '🇾':
                    message = await ctx.message.author.send("**Question 2:**\nDo you believe said government should be in charge of the market? (Y for yes, and N for no.)")
                    await message.add_reaction('🇾')
                    await message.add_reaction('🇳')
            if reaction2[0].emoji == '🇳':
                message = await ctx.message.author.send("**Question 2:**\nDo you believe in abolishing the concept of owning private property? (Y for yes, and N for no.)")
                await message.add_reaction('🇾')
                await message.add_reaction('🇳')
                def check(reaction, user):
                    return reaction.count == 2
                reaction2 = await z0diac.wait_for('reaction_add', check=check)
                if reaction2[0].emoji == '🇾':
                    message = await ctx.message.author.send( "**Question 3:**\nDo you believe said government should be in charge of the market? (Y for yes, and N for no.)")
                    await message.add_reaction('🇾')
                    await message.add_reaction('🇳')
        elif label == "bigdab" or label == "bigDab" or label == "big dab":
            await ctx.channel.send("bigdab is a shop item that allows you to post a full-sized dab instead of a tiny emote. This item costs you 10 EP.")
        elif label == "renamefuco" or label == "renameFuCo" or label == "rename FuCo":
            await ctx.channel.send("renamefuco is a shop item that allows you to rename FuCo, AKA BottomKek13 to whatever you desire; yes, he is not allowed to change whatever you give him. This item costs you 25 EP.")
        elif label == "membership" or label == "Membership" or label == "loungekey":
            await ctx.channel.send("The membership, AKA the Lounge Key, is a shop item that gives you the Member+ role and the ability to visit the off topic lounge. This item costs you 300 EP.")
        elif label == "ad" or label == "Ad" or label == "advertisement":
            await ctx.channel.send("ad is a shop item that allows you to advertise one message on the billboard channel for everyone to see. This item costs you 75 EP.")
        elif label == "subrole" or label == "Subrole" or label == "sub role":
            await ctx.channel.send("subrole is a shop item that gives you a role to tag yourself with. This item costs you 125 EP.")
        else:
            word = ctx.message.content[7:]
            meaningobject = dictionary.meaning(word)
            try:
                definition = next(iter(meaningobject.values()))[0]
                await ctx.channel.send(ctx.message.content[7:] + " means " + definition + ".")
            except:
                await ctx.channel.send(label + " isn't a real word, jackass.")
    else:
        await ctx.message.delete()
        await ctx.message.author.send("You cannot do that in this channel.")

@z0diac.event
async def on_raw_reaction_add(reaction, message, channel, reacter):
    #umbrella_roles = {discord.utils.get(message.guild.roles, id=420735827023495169)}
    if discord.utils.get(z0diac.get_all_channels(),id=420061566331781121).get_message(448475971553591300) == discord.utils.get(z0diac.get_all_channels(),id=420061566331781121).get_message(message):
        if reaction == 448475108290592769:
            await discord.utils.get(z0diac.get_all_members(), id=reacter).add_role(443242847681118218)
            await discord.utils.get(z0diac.get_all_members(), id=reacter).send('You have been given the ' + discord.utils.get(message.guild.roles, id=443242847681118218) + ' role.')
    elif discord.utils.get(z0diac.get_all_channels(), id=420061566331781121).get_message(448476172343574528) == discord.utils.get(z0diac.get_all_channels(),id=420061566331781121).get_message(message):
        if str(reaction) == '1⃣':
            await discord.utils.get(z0diac.get_all_members(), id=reacter).add_role(381176934131957760)
            await reacter.send('You have been given the ' + discord.utils.get(message.guild.roles, id=381176934131957760) + ' role.')
            await reacter.add_roles(discord.utils.get(channel.guild.roles, id=409483695582478348))
            await reacter.send('You are no longer in open-debate and now have access to lounge!')
    elif discord.utils.get(z0diac.get_all_channels(), id=420061566331781121).get_message(448476403638206474) == discord.utils.get(z0diac.get_all_channels(),id=420061566331781121).get_message(message):
        if str(reaction) == '1⃣':
            print('ye')
    elif str(reaction) == '📌' or str(reaction) == '📍':
        x = await discord.utils.get(z0diac.get_all_channels(), id=channel).get_message(message)
        embed = discord.Embed(title=(x.author.display_name + " (" + x.created_at.strftime("%Y-%m-%d %H:%M:%S") + ")"), color=x.author.color, description=x.content)
        embed.set_thumbnail(url=x.author.avatar_url)
        await z0diac.get_channel(446400765775314947).send(embed=embed)
    else:
        print('Fail')

@z0diac.command()
async def renamefuco(ctx):
    await ctx.channel.send('Thank you for participating in the free shop beta! You can now use your effort points to use this command. Simply do `/buy renamefuco [NAME]` to use the command!')

@z0diac.command()
async def buy(ctx):
    with open("dictionary.json", 'r+') as f:
        repkey = json.load(f)
        currentvalue_customer = repkey.get(str(ctx.message.author.id))
        if ctx.channel != z0diac.get_channel(432574353822056448):
            if ctx.message.content[5:] == 'bigdab' or ctx.message.content[:5] == 'dab':
                    dollar_amount = 5
                    if currentvalue_customer - dollar_amount >= 0:
                        repkey[str(ctx.message.author.id)] = currentvalue_customer - dollar_amount
                        f.seek(0)
                        json.dump(repkey, f)
                        f.truncate()
                        with open('bigdab.png','rb') as image:
                            await ctx.channel.send(file=image)
                    else:
                        await ctx.channel.send('You need 25 EP to do that!')
            elif ctx.message.content[5:15] == 'renamefuco':
                if ctx.message.author != discord.utils.get(ctx.guild.members, id=346821778829475861):
                    fuco = ctx.guild.get_member(346821778829475861)
                    beforefuco = fuco.display_name
                    dollar_amount = 25
                    if currentvalue_customer - dollar_amount >= 0:
                            repkey[str(ctx.message.author.id)] = currentvalue_customer - dollar_amount
                            f.seek(0)
                            json.dump(repkey, f)
                            f.truncate()
                    try:
                        await fuco.edit(nick=ctx.message.content[16:])
                        await ctx.channel.trigger_typing()
                        time.sleep(3)
                        afterfuco = fuco.display_name
                        await ctx.channel.send(beforefuco + ', more like ' + afterfuco + '!')
                    except discord.ext.commands.errors.CommandInvokeError:
                        await ctx.channel.send("Too long.")
                else:
                    await ctx.channel.send("Nice try, FuCo.")
            elif ctx.message.content[5:12] == 'subrole':
                dollar_amount = (75 + len(ctx.message.author.roles) * 50)
                if currentvalue_customer - dollar_amount >= 0:
                    repkey[str(ctx.message.author.id)] = currentvalue_customer - dollar_amount
                    f.seek(0)
                    json.dump(repkey, f)
                    f.truncate()
                    role_name = await ctx.guild.create_role(name=ctx.message.content[12:],mentionable=True)
                    await ctx.message.author.add_roles(role_name)
                    await ctx.channel.send('You have been given the' + ctx.message.content[12:] + ' role.')
                else:
                    await ctx.channel.send('You need ' + str(dollar_amount) + ' EP to do that!')
            elif ctx.message.content[5:9] == 'gift':
                try:
                    with open("dictionary.json", 'r+') as f:
                        repkey = json.load(f)
                        currentvalue_recipient = repkey.get(str(ctx.message.raw_mentions[0]))
                        currentvalue_giver = repkey.get(str(ctx.message.author.id))
                        dollar_amount = ctx.message.content.find('>') + 1
                        if ctx.message.raw_mentions[0] != ctx.message.author.id:
                            if currentvalue_giver - int(ctx.message.content[dollar_amount:]) >= 0:
                                if int(ctx.message.content[dollar_amount:]) > 0:
                                    repkey[str(ctx.message.author.id)] = (
                                    currentvalue_giver - int(ctx.message.content[dollar_amount:]))
                                    f.seek(0)
                                    json.dump(repkey, f)
                                    f.truncate()
                                    with open("dictionary.json", 'r+') as file:
                                        repkey2 = json.load(file)
                                        repkey2[str(ctx.message.raw_mentions[0])] = (
                                        currentvalue_recipient + int(ctx.message.content[dollar_amount:]))
                                        file.seek(0)
                                        json.dump(repkey2, file)
                                        file.truncate()
                                    payment = ctx.message.content[(ctx.message.content.find('>') + 1):]
                                    await ctx.channel.send( 'You have successfully gifted ' + (str(ctx.message.mentions[0]))[:-5] + payment + ' Effort Points.')
                                else:
                                    await ctx.channel.send('Gifts must be a positive number, nice try.')
                            else:
                                print('You cannot afford that!')
                        else:
                            await ctx.channel.send("Nice try, but you can't give yourself cash.")
                except IndexError or ValueError:
                    await ctx.channel.send('Something went wrong, remember to format your message as: /buy gift [mentioned person] [number].')
                    traceback.print_exc()


@z0diac.command()
async def vote(ctx):
    if ctx.message.content[6:12] == 'speaker':
        if discord.utils.get(ctx.guild.roles, id=416369684179320834) in ctx.message.author.roles or discord.utils.get(ctx.guild.roles, id=443242847681118218) in ctx.message.author.roles or discord.utils.get(ctx.guild.roles, id=443242847681118218) in ctx.message.author.roles or discord.utils.get(ctx.guild.roles, id=420735827023495169) in ctx.message.author.roles or discord.utils.get(ctx.guild.roles, id=382557327892676619) in ctx.message.author.roles or discord.utils.get(ctx.guild.roles, id=381178125591117827) in ctx.message.author.roles:
            await ctx.message.channel.send('Mention who would you like to vote for for speaker:\nBladeHoldin - Libertarian Socialist\nThe Firebird - Green\nBearTheIndependent - Social Democrat\nTsarNicky - Paternalist')




z0diac.run("MzgzMzg1MTk4NTM0MDY2MTg3.DeSjjg.UTV6BKxXzMrqIVmgMDahKsfZDzs")
