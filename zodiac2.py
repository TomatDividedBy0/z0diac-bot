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
            embed = discord.Embed(color=discord.utils.get(ctx.guild.roles,id=443242847681118218).color)
            embed.set_author(name="Socialist",icon_url=z0diac.get_emoji(454666012860743695).url)
            embed.add_field(name="**Type:**", value="Umbrella Role")
            embed.add_field(name="**Wing:**", value="Socialist")
            embed.add_field(name="**Representative:**", value="sparkle#5001")
            embed.add_field(name="**Members:**", value=str(len(discord.utils.get(ctx.guild.roles,id=443242847681118218).members)))
            embed.add_field(name="**Description:**", value="Socialists believe in the public ownership of the means of production. They are commonly found on the far-left end of the compass, with varying degrees of authoritarianism/libertarianism.")
            message = await ctx.channel.send(embed=embed)
        elif label == "Classical Liberal" or label == "classical liberal" or label == "classical lib" or label == "Classical liberal" or label == "Classical Lib" or label == "Classical lib":
            embed = discord.Embed(color=discord.utils.get(ctx.guild.roles,id=381177029464293386).color)
            embed.set_author(name="Classical Liberal",icon_url=z0diac.get_emoji(454665209009668097).url)
            embed.add_field(name="**Type:**", value="Umbrella Role")
            embed.add_field(name="**Wing:**", value="Liberal")
            embed.add_field(name="**Representative:**", value="Revolt#8500")
            embed.add_field(name="**Members:**", value=str(len(discord.utils.get(ctx.guild.roles,id=381177029464293386).members)))
            embed.add_field(name="**Description:**", value="Classical liberals adhere strongly to the rights of the individual, however, unlike libertarians, they are a lot more moderate on the free market. You'll usually find them straight down from center or near center.")
            message = await ctx.channel.send(embed=embed)
        elif label == "Nationalist" or label == "nationalist":
            embed = discord.Embed(color=discord.utils.get(ctx.guild.roles, id=427819576882102273).color)
            embed.set_author(name="Nationalist", icon_url=z0diac.get_emoji(454663855809757195).url)
            embed.add_field(name="**Type:**", value="Umbrella Role")
            embed.add_field(name="**Wing:**", value="Liberal")
            embed.add_field(name="**Representative:**", value="Gunnz011#7212")
            embed.add_field(name="**Members:**", value=str(len(discord.utils.get(ctx.guild.roles, id=427819576882102273).members)))
            embed.add_field(name="**Description:**", value="Nationalists believe in putting their own country or group first above others. They are often protectionist, and come in many different variants from Civic Nationalists to Ethnonationalists.")
            message = await ctx.channel.send(embed=embed)
        elif label == "Right Libertarian" or label == "Libertarian" or label == "libertarian" or label == "right libertarian":
            embed = discord.Embed(color=discord.utils.get(ctx.guild.roles, id=381177107616759810).color)
            embed.set_author(name="Libertarian", icon_url=z0diac.get_emoji(454664092305588235).url)
            embed.add_field(name="**Type:**", value="Umbrella Role")
            embed.add_field(name="**Wing:**", value="Liberal")
            embed.add_field(name="**Representative:**", value="BulbaBlin#7776")
            embed.add_field(name="**Members:**", value=str(len(discord.utils.get(ctx.guild.roles, id=381177107616759810).members)))
            embed.add_field(name="**Description:**", value="Libertarians tend to favor solutions that involve the free market and the individual over government intervention, detesting excess public spending and tax hikes. They are found everywhere on the bottom right of the compass.")
            message = await ctx.channel.send(embed=embed)
        elif label == "Paleoconservative" or label == "paleocon" or label == "paleoconservative" or label == "paleocon":
            embed = discord.Embed(color=discord.utils.get(ctx.guild.roles, id=424645022927945736).color)
            embed.set_author(name="Paleoconservative", icon_url=z0diac.get_emoji(454662578488999937).url)
            embed.add_field(name="**Type:**", value="Umbrella Role")
            embed.add_field(name="**Wing:**", value="Reactionary")
            embed.add_field(name="**Representative:**", value="saldol-1104#5500")
            embed.add_field(name="**Members:**", value=str(len(discord.utils.get(ctx.guild.roles, id=424645022927945736).members)))
            embed.add_field(name="**Description:**", value="Paleoconservatives, also known as the Old Right, date back to the early 20th century in their beliefs. They place social tradition and economic nonintervention above all else, often being in the top right of the compass.")
            message = await ctx.channel.send(embed=embed)
        elif label == "LibtSoc" or label == "Libertarian Socialist" or label == "Libertarian Socialist" or label == "libertarian socialist":
            embed = discord.Embed(color=discord.utils.get(ctx.guild.roles, id=382557327892676619).color)
            embed.set_author(name="Libertarian Socialist", icon_url=z0diac.get_emoji(454663573386559499).url)
            embed.add_field(name="**Type:**", value="Umbrella Role")
            embed.add_field(name="**Wing:**", value="Socialist")
            embed.add_field(name="**Representative:**", value="Blade Holdin#3961")
            embed.add_field(name="**Members:**", value=str(len(discord.utils.get(ctx.guild.roles, id=382557327892676619).members)))
            embed.add_field(name="**Description:**", value="Libertarian Socialists/AnComs are distrusting of authority, opposing both the state and corporate power as a means to liberate people.")
            message = await ctx.channel.send(embed=embed)
        elif label == "SocDem" or label == "socdem" or label == "social democrat" or label == "Social Democrat" or label == "Social democrat" or label == "Socdem":
            embed = discord.Embed(color=discord.utils.get(ctx.guild.roles, id=381178125591117827).color)
            embed.set_author(name="Social Democrat", icon_url=z0diac.get_emoji(454666536142110721).url)
            embed.add_field(name="**Type:**", value="Umbrella Role")
            embed.add_field(name="**Wing:**", value="Socialist")
            embed.add_field(name="**Representative:**", value="Bear+Maiden=Faire#3513")
            embed.add_field(name="**Members:**", value=str(len(discord.utils.get(ctx.guild.roles, id=381178125591117827).members)))
            embed.add_field(name="**Description:**", value="Social Democrats believe in using government as a tool to bring about social progress and change. They lean authoritative, intersect with social justice, and are typically found on the left.")
            message = await ctx.channel.send(embed=embed)
        elif label == "green" or label == "Green" or label == "left libertarian":
            embed = discord.Embed(color=discord.utils.get(ctx.guild.roles, id=420735827023495169).color)
            embed.set_author(name="Green", icon_url=z0diac.get_emoji(454664511173951494).url)
            embed.add_field(name="**Type:**", value="Umbrella Role")
            embed.add_field(name="**Wing:**", value="Socialist")
            embed.add_field(name="**Representative:**", value="The Firebird#7278")
            embed.add_field(name="**Members:**", value=str(len(discord.utils.get(ctx.guild.roles, id=420735827023495169).members)))
            embed.add_field(name="**Description:**", value="Greens tend to be less about the economic liberty and more about the social and infrastructure liberty, especially on envrionmental issues. The open source community and net neutrality opponents are good examples of Greens.")
            message = await ctx.channel.send(embed=embed)
        elif label == "Neoliberal" or label == "neolib" or label == "neoliberal":
            embed = discord.Embed(color=discord.utils.get(ctx.guild.roles, id=381177002033676298).color)
            embed.set_author(name="Neoliberal", icon_url=z0diac.get_emoji(454666880771424258).url)
            embed.add_field(name="**Type:**", value="Umbrella Role")
            embed.add_field(name="**Wing:**", value="Liberal")
            embed.add_field(name="**Representative:**", value="Webhobo#4708")
            embed.add_field(name="**Members:**", value=str(len(discord.utils.get(ctx.guild.roles, id=381177002033676298).members)))
            embed.add_field(name="**Description:**", value="Neoliberalism mixes aspects of progressivism and classical liberalism to create an ideology that's moderate, pragmatic, and often focused on values such as globalism, lower government spending, and deregulation.")
            message = await ctx.channel.send(embed=embed)
        elif label == "centrist" or label == "Centrist":
            embed = discord.Embed(color=discord.utils.get(ctx.guild.roles, id=381176934131957760).color)
            embed.set_author(name="Centrist", icon_url=z0diac.get_emoji(454666611568410634).url)
            embed.add_field(name="**Type:**", value="Umbrella Role")
            embed.add_field(name="**Wing:**", value="Liberal")
            embed.add_field(name="**Representative:**", value="BowlOfPepper#2090")
            embed.add_field(name="**Members:**", value=str(len(discord.utils.get(ctx.guild.roles, id=381176934131957760).members)))
            embed.add_field(name="**Description:**", value="Centrists don't particularly lean any noticeable amount on the left/right scale; their policies are often moderate, and they focus on compromise over ideological passion. They can be anywhere on the authoritarian/libertarian scale.")
            message = await ctx.channel.send(embed=embed)
        elif label == "neocon" or label == "neoconservative" or label == "Neoconservative" or label == "Neocon":
            embed = discord.Embed(color=discord.utils.get(ctx.guild.roles, id=381176967631863810).color)
            embed.set_author(name="Neoconservative", icon_url=z0diac.get_emoji(454664747464392724).url)
            embed.add_field(name="**Type:**", value="Umbrella Role")
            embed.add_field(name="**Wing:**", value="Liberal")
            embed.add_field(name="**Representative:**", value="Kaiser Wilhelm II#3444")
            embed.add_field(name="**Members:**", value=str(len(discord.utils.get(ctx.guild.roles, id=381176967631863810).members)))
            embed.add_field(name="**Description:**", value="Neoconservatism is a foreign policy theory that builds on the idea that it's a democratic country's duty to spread its values through foreign intervention. On most issues but foreign policy, they tend to be more moderate.")
            message = await ctx.channel.send(embed=embed)
        elif label == "Paternalist" or label  == "paternalist":
            embed = discord.Embed(color=discord.utils.get(ctx.guild.roles, id=416369684179320834).color)
            embed.set_author(name="Paternalist", icon_url=z0diac.get_emoji(454663251633111050).url)
            embed.add_field(name="**Type:**", value="Umbrella Role")
            embed.add_field(name="**Wing:**", value="Reactionary")
            embed.add_field(name="**Representative:**", value="PaxBritannicus#3672")
            embed.add_field(name="**Members:**", value=str(len(discord.utils.get(ctx.guild.roles, id=416369684179320834).members)))
            embed.add_field(name="**Description:**", value="Paternalists believe in the state taking a parent role, being authoritative on social policy, but interventionist economically.")
            message = await ctx.channel.send(embed=embed)
        elif label == "Theologue" or label == "theologue":
            embed = discord.Embed(color=discord.utils.get(ctx.guild.roles, id=409124661272641536).color)
            embed.set_author(name="Theologue", icon_url=z0diac.get_emoji(454667115601854474).url)
            embed.add_field(name="**Type:**", value="Umbrella Role")
            embed.add_field(name="**Wing:**", value="Reactionary")
            embed.add_field(name="**Representative:**", value="JacolManuki#0703")
            embed.add_field(name="**Members:**", value=str(len(discord.utils.get(ctx.guild.roles, id=409124661272641536).members)))
            embed.add_field(name="**Description:**", value="Theologues are socially conservative, but vary widely on their economic policies. This includes Distributists, Christian Democrats, and right-theologues. Their main deciding factor in voting is their religion.")
            message = await ctx.channel.send(embed=embed)
        elif label == "Third Positioner" or label == "Third Positioner":
            embed = discord.Embed(color=discord.utils.get(ctx.guild.roles, id=448633320431943682).color)
            embed.set_author(name="Third Positioner", icon_url=z0diac.get_emoji(454665463847321602).url)
            embed.add_field(name="**Type:**", value="Umbrella Role")
            embed.add_field(name="**Wing:**", value="Reactionary")
            embed.add_field(name="**Representative:**", value="Militaristic Cezar#6488")
            embed.add_field(name="**Members:**", value=str(len(discord.utils.get(ctx.guild.roles, id=448633320431943682).members)))
            embed.add_field(name="**Description:**", value="Third Positioners believe that the control of economic and social issues is best kept in the hands of a few or singular entities; they are economically incredibly authoritarian and interventionist, but differ on conservative/progressive.")
            message = await ctx.channel.send(embed=embed)
        elif label == "On Sale" or label == "for sale" or label == "For sale" or label == "forsale" or label == "Forsale" or label == "forSale":
            embed = discord.Embed(title="**Currently, we have the following items:**",description=" -ad\n -renamesaldol\n -memberplus\n -bigdab\n -subrole.\n -omegalounge\n Do `/whatis [Item]` to learn about pricing and descriptions.")
            embed.set_author(name="Effort Points Shop")
            message = await ctx.channel.send(embed=embed)
        elif label == "specs" or label == "Specs" or label == "yourspecs" or label== "your specs":
            embed = discord.Embed(color=ctx.guild.get_member(383385198534066187).color)
            embed.set_author(name="z0diac-bot's Specs", icon_url=ctx.guild.get_member(383385198534066187).avatar_url)
            embed.add_field(name="**CPU:**", value="Opteron 3365")
            embed.add_field(name="**GPU:**", value="Radeon R7 360")
            embed.add_field(name="**HDD:**", value="320GB HDD")
            embed.add_field(name="**RAM:**", value='8GB DDR3')
            embed.add_field(name="**OS:**", value="Kubuntu")
            message = await ctx.channel.send(embed=embed)
        elif label == "myBalance" or label == "mybalance" or label == "my balance":
            with open("dictionary.json", 'r') as f:
                repkey = json.load(f)
            with open("dp.json", "r") as file:
                dpkey = json.load(file)
            embed = discord.Embed(color=ctx.message.author.color)
            embed.set_author(name=(ctx.message.author.display_name + "'s Balance" ), icon_url=ctx.message.author.avatar_url)
            embed.add_field(name="**Daily Points:**", value=(str(dpkey.get(str(ctx.message.author.id)))))
            embed.add_field(name="**Effort Points:**", value=str(repkey.get(str(ctx.message.author.id))))
            message = await ctx.channel.send(embed=embed)
        elif label == "myideology" or label == "my ideology" or label == "myIdeology":
            await ctx.message.delete()
            message_to = await ctx.message.author.send("Welcome to the official compact edition of the PWH political test. \nYou will be asked various questions on your values to determine your ideology. You will be presented with either a yes or a no option. Simply click the corresponding button to answer said question. To begin, click the green check mark.")
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
                await message_3.remove_reaction('🇳',z0diac.user)
                message = await ctx.message.author.send("**Question 2:**\nDo you believe that Lockean rights are part of, if not the inalienable human rights? (Y for yes, and N for no.)")
                await message.add_reaction('🇾')
                await message.add_reaction('🇳')
                def check(reaction, user):
                    return reaction.count == 2
                reaction3 = await z0diac.wait_for('reaction_add', check=check)
                if reaction3[0].emoji == '🇾':
                    await message.remove_reaction('🇳', member=z0diac.user)
                    message = await ctx.message.author.send("**Question 3:**\nDo you believe rights do not expand beyond protections *from* government tyranny? (Y for yes, and N for no.)")
                    await message.add_reaction('🇾')
                    await message.add_reaction('🇳')
                    def check(reaction, user):
                        return reaction.count == 2
                    reaction7 = await z0diac.wait_for('reaction_add', check=check)
                    if reaction7[0].emoji == '🇾':
                        await message.remove_reaction('🇳', member=z0diac.user)
                        message = await ctx.message.author.send("**Question 4:**\nDo you believe our children should be taught to respect their country? (Y for yes, and N for no.)")
                        await message.add_reaction('🇾')
                        await message.add_reaction('🇳')
                        def check(reaction, user):
                            return reaction.count == 2
                        reaction9 = await z0diac.wait_for('reaction_add', check=check)
                        if reaction9[0].emoji == '🇾':
                            await message.remove_reaction('🇳', member=z0diac.user)
                            message = await ctx.message.author.send("**Question 5:**\nDo you respect your country for its founding moral values over its founding political values? (Y for yes, and N for no.)")
                            await message.add_reaction('🇾')
                            await message.add_reaction('🇳')
                            def check(reaction, user):
                                return reaction.count == 2
                            reaction14 = await z0diac.wait_for('reaction_add', check=check)
                            if reaction14[0].emoji == '🇾':
                                await message.remove_reaction('🇳', member=z0diac.user)
                                message = await ctx.message.author.send("**Question 6:**\nDo you believe it is your nation's moral duty to spread its moral/political values around the world through foreign intervention? (Y for yes, and N for no.)")
                                await message.add_reaction('🇾')
                                await message.add_reaction('🇳')
                                def check(reaction, user):
                                    return reaction.count == 2
                                reaction15 = await z0diac.wait_for('reaction_add', check=check)
                                if reaction15[0].emoji == '🇾':
                                    await message.remove_reaction('🇳', member=z0diac.user)
                                    message = await ctx.message.author.send("Your umbrella role is... **Nationalist**. Your subrole is... **Imperial Conservative**. If you have more questions or a more specific ideology to add, please DM Dakota.")
                                if reaction15[0].emoji == '🇳':
                                    await message.remove_reaction('🇾', member=z0diac.user)
                                    message = await ctx.message.author.send("Your umbrella role is... **Paleoconservative**. If you have more questions or a more specific ideology to add, please DM Dakota.")
                            if reaction14[0].emoji == '🇳':
                                await message.remove_reaction('🇾', member=z0diac.user)
                                message = await ctx.message.author.send("Your umbrella role is... **Nationalist**. Your subrole is... **Civic Nationalist**. If you have more questions or a more specific ideology to add, please DM Dakota.")
                        if reaction9[0].emoji == '🇳':
                            await message.remove_reaction('🇾', member=z0diac.user)
                            message = await ctx.message.author.send("**Question 5:**\nDo you believe that the market's freedom is equally as important as an individual's freedom? (Y for yes, and N for no.)")
                            await message.add_reaction('🇾')
                            await message.add_reaction('🇳')
                            def check(reaction, user):
                                return reaction.count == 2
                            reaction10 = await z0diac.wait_for('reaction_add', check=check)
                            if reaction10[0].emoji == '🇾':
                                await message.remove_reaction('🇳', member=z0diac.user)
                                message = await ctx.message.author.send("**Question 6:**\nDo you support the ownership of land? (Y for yes, and N for no.)")
                                await message.add_reaction('🇾')
                                await message.add_reaction('🇳')
                                def check(reaction, user):
                                    return reaction.count == 2
                                reaction11 = await z0diac.wait_for('reaction_add', check=check)
                                if reaction11[0].emoji == '🇾':
                                    await message.remove_reaction('🇳', member=z0diac.user)
                                    message = await ctx.message.author.send("**Question 7:**\nDo you support global military intervention? (Y for yes, and N for no.)")
                                    await message.add_reaction('🇾')
                                    await message.add_reaction('🇳')
                                    def check(reaction, user):
                                        return reaction.count == 2
                                    reaction17 = await z0diac.wait_for('reaction_add', check=check)
                                    if reaction17[0].emoji == '🇾':
                                        await message.remove_reaction('🇳', member=z0diac.user)
                                        message = await ctx.message.author.send("Your umbrella role is... **Libertarian**. Your subrole is... **Neolibertarian**. If you have more questions or a more specific ideology to add, please DM Dakota.")
                                    if reaction17[0].emoji == '🇳':
                                        await message.remove_reaction('🇾', member=z0diac.user)
                                        message = await ctx.message.author.send("Your umbrella role is... **Libertarian**. Your subrole is... **Paleolibertarian**. If you have more questions or a more specific ideology to add, please DM Dakota.")
                                if reaction11[0].emoji == '🇳':
                                    await message.remove_reaction('🇾', member=z0diac.user)
                                    message = await ctx.message.author.send("Your umbrella role is... **Libertarian**. Your subrole is... **Geolibertarian**. If you have more questions or a more specific ideology to add, please DM Dakota.")
                            if reaction10[0].emoji == '🇳':
                                await message.remove_reaction('🇾', member=z0diac.user)
                                message = await ctx.message.author.send("**Question 6:**\nDo you believe reason should always take precedent over all else, including social norms and dogma? (Y for yes, and N for no.)")
                                await message.add_reaction('🇾')
                                await message.add_reaction('🇳')
                                def check(reaction, user):
                                    return reaction.count == 2
                                reaction12 = await z0diac.wait_for('reaction_add', check=check)
                                if reaction12[0].emoji == '🇳':
                                    await message.remove_reaction('🇾', member=z0diac.user)
                                    message = await ctx.message.author.send("**Question 7:**\nIs religion the largest driving factor in your political beliefs?")
                                    def check(reaction, user):
                                        return reaction.count == 2
                                    reaction13 = await z0diac.wait_for('reaction_add', check=check)
                                    if reaction13[0].emoji == '🇳':
                                        await message.remove_reaction('🇾', member=z0diac.user)
                                        message = await ctx.message.author.send("Your umbrella role is... **Classical Liberal**. If you have more questions or a more specific ideology to add, please DM Dakota.")
                                    if reaction13[0].emoji == '🇾':
                                        await message.remove_reaction('🇳', member=z0diac.user)
                                        message = await ctx.message.author.send("Your umbrella role is... **Theologue**. Your subrole is... **Theodemocrat**. If you have more questions or a more specific ideology to add, please DM Dakota.")
                                if reaction12[0].emoji == '🇾':
                                    await message.remove_reaction('🇳', member=z0diac.user)
                                    message = await ctx.message.author.send("Your umbrella role is... **Classical Liberal**. Your subrole is... **Modernist**. If you have more questions or a more specific ideology to add, please DM Dakota.")
                    if reaction7[0].emoji == '🇳':
                        await message.remove_reaction('🇾', member=z0diac.user)
                        message = await ctx.message.author.send("**Question 4:**\nDo you support companies being able to enforce political correctness upon their employees? (Y for yes, and N for no.)")
                        await message.add_reaction('🇾')
                        await message.add_reaction('🇳')
                        def check(reaction, user):
                            return reaction.count == 2
                        reaction18 = await z0diac.wait_for('reaction_add', check=check)
                        if reaction18[0].emoji == '🇾':
                            await message.remove_reaction('🇳', member=z0diac.user)
                            message = await ctx.message.author.send("**Question 5:**\nDo you support the government being involved in pushing social justice? (Y for yes, and N for no.)")
                            await message.add_reaction('🇾')
                            await message.add_reaction('🇳')
                            def check(reaction, user):
                                return reaction.count == 2
                            reaction19 = await z0diac.wait_for('reaction_add', check=check)
                            if reaction19[0].emoji == '🇾':
                                await message.remove_reaction('🇳', member=z0diac.user)
                                message = await ctx.message.author.send("**Question 6:**\nShould the government take an active role in being the dealer of economic justice? (Y for yes, and N for no.)")
                                await message.add_reaction('🇾')
                                await message.add_reaction('🇳')
                                def check(reaction, user):
                                    return reaction.count == 2
                                reaction22 = await z0diac.wait_for('reaction_add', check=check)
                                if reaction22[0].emoji == '🇾':
                                    await message.remove_reaction('🇳', member=z0diac.user)
                                    message = await ctx.message.author.send("Your umbrella role is... **Social Democracy**. Your subrole is... **Paternalistic Progressivism**. If you have more questions or a more specific ideology to add, please DM Dakota.")
                                if reaction22[0].emoji == '🇳':
                                    await message.remove_reaction('🇾', member=z0diac.user)
                                    message = await ctx.message.author.send("**Question 7**\nShould we fully embrace the international community, even in times where it does not directly benefit us?")
                                    await message.add_reaction('🇾')
                                    await message.add_reaction('🇳')
                                    def check(reaction, user):
                                        return reaction.count == 2
                                    reaction23 = await z0diac.wait_for('reaction_add', check=check)
                                    if reaction23[0].emoji == '🇾':
                                        await message.remove_reaction('🇳', member=z0diac.user)
                                        message = await ctx.message.author.send("**Question 8:** Is it western society's job to act as policeman of the rest of the world?")
                                        await message.add_reaction('🇾')
                                        await message.add_reaction('🇳')
                                        def check(reaction, user):
                                            return reaction.count == 2
                                        reaction40 = await z0diac.wait_for('reaction_add', check=check)
                                        if reaction40[0].emoji == '🇾':
                                            await message.remove_reaction('🇳', member=z0diac.user)
                                            message = await ctx.message.author.send("Your umbrella role is... **Neoconservative**. Your subrole is... **Neoconservative Neoliberal**. If you have more questions or a more specific ideology to add, please DM Dakota.")
                                            await message.add_reaction('🇾')
                                            await message.add_reaction('🇳')
                                        if reaction40[0].emoji == '🇳':
                                            await message.remove_reaction('🇾', member=z0diac.user)
                                            message = await ctx.message.author.send("Your umbrella role is... **Neoliberal**. Your subrole is... **Diplomatic Neoliberal**. If you have more questions or a more specific ideology to add, please DM Dakota.")
                                            await message.add_reaction('🇾')
                                            await message.add_reaction('🇳')
                                    if reaction23[0].emoji == '🇳':
                                        await message.remove_reaction('🇾', member=z0diac.user)
                                        message = await ctx.message.author.send("**Question 9:**\n Do you believe society has to be fundamentally changed in order to progress?")
                                        await message.add_reaction('🇾')
                                        await message.add_reaction('🇳')
                                        def check(reaction, user):
                                            return reaction.count == 2
                                        reaction24 = await z0diac.wait_for('reaction_add', check=check)
                                        if reaction24[0].emoji == '🇾':
                                            await message.remove_reaction('🇳', member=z0diac.user)
                                            message = await ctx.message.author.send("**Question 10:** Can someone say for sure which entity or group should hold power?")
                                            await message.add_reaction('🇾')
                                            await message.add_reaction('🇳')
                                            reaction26 = await z0diac.wait_for('reaction_add', check=check)
                                            if reaction26[0].emoji == '🇾':
                                                await message.remove_reaction('🇳', member=z0diac.user)
                                                message = await ctx.message.author.send("Your umbrella role is... **Centrist**. Your subrole is... **Technocratic Liberal**. If you have more questions or a more specific ideology to add, please DM Dakota.")
                                            if reaction26[0].emoji == '🇳':
                                                await message.remove_reaction('🇾', member=z0diac.user)
                                                message = await ctx.message.author.send("Your umbrella role is... **Centrist**. Your subrole is... **Radical Pluralist**. If you have more questions or a more specific ideology to add, please DM Dakota.")
                                        if reaction24[0].emoji == '🇳':
                                            await message.remove_reaction('🇾', member=z0diac.user)
                                            message = await ctx.message.author.send("Your umbrella role is... **Centrist**. Your subrole is... **Ordoliberal**. If you have more questions or a more specific ideology to add, please DM Dakota.")
                            if reaction19[0].emoji == '🇳':
                                await message.remove_reaction('🇾', member=z0diac.user)
                                await message.remove_reaction('🇾', member=z0diac.user)
                                message = await ctx.message.author.send("**Question 9:**\n Do you believe society has to be fundamentally changed in order to progress?")
                                await message.add_reaction('🇾')
                                await message.add_reaction('🇳')
                                def check(reaction, user):
                                    return reaction.count == 2
                                reaction29 = await z0diac.wait_for('reaction_add', check=check)
                                if reaction29[0].emoji == '🇾':
                                    await message.remove_reaction('🇳', member=z0diac.user)
                                    message = await ctx.message.author.send("**Question 10:** Can someone say for sure which entity or group should hold power?")
                                    await message.add_reaction('🇾')
                                    await message.add_reaction('🇳')
                                    reaction30 = await z0diac.wait_for('reaction_add', check=check)
                                    if reaction30[0].emoji == '🇾':
                                        await message.remove_reaction('🇳', member=z0diac.user)
                                        message = await ctx.message.author.send("Your umbrella role is... **Centrist**. Your subrole is... **Technocratic Centrist**. If you have more questions or a more specific ideology to add, please DM Dakota.")
                                    if reaction30[0].emoji == '🇳':
                                        await message.remove_reaction('🇾', member=z0diac.user)
                                        message = await ctx.message.author.send("Your umbrella role is **Centrist**. Your subrole is... **Radical Pluralist**. If you have more questions or a more specific ideology to add, please DM Dakota.")
                                if reaction29[0].emoji == '🇳':
                                    await message.remove_reaction('🇾', member=z0diac.user)
                                    message = await ctx.message.author.send("Your umbrella role is... **Centrist**. Your subrole is... **Ordoliberal**. If you have more questions or a more specific ideology to add, please DM Dakota.")
                        if reaction18[0].emoji == '🇳':
                            await message.remove_reaction('🇾', member=z0diac.user)
                            message = await ctx.message.author.send("**Question 5:**\nDo you believe in upholding tradition at the expense of social liberty? (Y for yes, and N for no.)")
                            await message.add_reaction('🇾')
                            await message.add_reaction('🇳')
                            def check(reaction, user):
                                return reaction.count == 2
                            reaction28 = await z0diac.wait_for('reaction_add', check=check)
                            if reaction28[0].emoji == '🇾':
                                await message.remove_reaction('🇳', member=z0diac.user)
                                message = await ctx.message.author.send("Your umbrella role is either... **Paternalist or Theologue**. Your subrole is... **Paternalistic Theodemocrat**. If you have more questions or a more specific ideology to add, please DM Dakota.")
                            if reaction28[0].emoji == '🇳':
                                await message.remove_reaction('🇾', member=z0diac.user)
                                message = await ctx.message.author.send("Your umbrella role is... **Green**. Your subrole is... **Cultural Libertarian**. If you have more questions or a more specific ideology to add, please DM Dakota.")
                if reaction3[0].emoji == '🇳':
                    await message.remove_reaction('🇾', member=z0diac.user)
                    message = await ctx.message.author.send("**Question 3:**\nDo you believe government should be controlled by the strongest/smartest/best? (Y for yes, and N for no.)")
                    await message.add_reaction('🇾')
                    await message.add_reaction('🇳')
                    def check(reaction, user):
                        return reaction.count == 2
                    reaction32 = await z0diac.wait_for('reaction_add', check=check)
                    if reaction32[0].emoji == '🇾':
                        await message.remove_reaction('🇳', member=z0diac.user)
                        message = await ctx.message.author.send("**Question 4:**\nDo you see your ethnicity as the greatest?")
                        await message.add_reaction('🇾')
                        await message.add_reaction('🇳')
                        def check(reaction, user):
                            return reaction.count == 2
                        reaction34 = await z0diac.wait_for('reaction_add', check=check)
                        if reaction34[0].emoji == '🇾':
                            await message.remove_reaction('🇳', member=z0diac.user)
                            message = await ctx.message.author.send("Your umbrella role is... **Third Positioner**. Your subrole is... **National Socialist**. If you have more questions or a more specific ideology to add, please DM Dakota.")
                        if reaction34[0].emoji == '🇳':
                            await message.remove_reaction('🇾', member=z0diac.user)
                            message = await ctx.message.author.send("**Question 5:**\nIs it justifiable to impose your religion onto others using the state?")
                            await message.add_reaction('🇾')
                            await message.add_reaction('🇳')
                            def check(reaction, user):
                                return reaction.count == 2
                            reaction34 = await z0diac.wait_for('reaction_add', check=check)
                            if reaction34[0].emoji == '🇾':
                                await message.remove_reaction('🇳', member=z0diac.user)
                                message = await ctx.message.author.send("Your umbrella role is... **Theologue**. Your subrole is... **Theocrat**. If you have more questions or a more specific ideology to add, please DM Dakota.")
                            if reaction34[0].emoji == '🇳':
                                await message.remove_reaction('🇾', member=z0diac.user)
                                message = await ctx.message.author.send("**Question 6:**\nAre philosophers or other wise men the only ones capable of properly ruling the people?")
                                await message.add_reaction('🇾')
                                await message.add_reaction('🇳')
                                def check(reaction, user):
                                    return reaction.count == 2
                                reaction36 = await z0diac.wait_for('reaction_add', check=check)
                                if reaction36[0].emoji == '🇾':
                                    await message.remove_reaction('🇳', member=z0diac.user)
                                    message = await ctx.message.author.send("Your umbrella role is... **Third Positioner**. Your subrole is... **Noocrat**. If you have more questions or a more specific ideology to add, please DM Dakota.")
                                if reaction36[0].emoji == '🇳':
                                    await message.remove_reaction('🇾', member=z0diac.user)
                                    message = await ctx.message.author.send("Your umbrella role is... **Third Positioner**. Your subrole is... **Monarchist**. If you have more questions or a more specific ideology to add, please DM Dakota.")
                                    await message.add_reaction('🇾')
                                    await message.add_reaction('🇳')
                    if reaction32[0].emoji == '🇳':
                        await message.remove_reaction('🇾', member=z0diac.user)
                        message = await ctx.message.author.send("**Question 4:**\nShould the government serve the working class over economic interests?")
                        await message.add_reaction('🇾')
                        await message.add_reaction('🇳')
                        def check(reaction, user):
                            return reaction.count == 2
                        reaction33 = await z0diac.wait_for('reaction_add', check=check)
                        if reaction33[0].emoji == '🇾':
                            await message.remove_reaction('🇳', member=z0diac.user)
                            message = await ctx.message.author.send("**Question 5: ")
                            await message.add_reaction('🇾')
                            await message.add_reaction('🇳')
                            def check(reaction, user):
                                return reaction.count == 2
                            reaction41 = await z0diac.wait_for('reaction_add', check=check)
                            if reaction41[0].emoji == '🇾':
                                await message.remove_reaction('🇳', member=z0diac.user)
                                message = await ctx.message.author.send("Your umbrella role is... **Third Positioner**. Your subrole is... **Marxist-Leninist**. If you have more questions or a more specific ideology to add, please DM Dakota.")
                            if reaction41[0].emoji == '🇳':
                                await message.remove_reaction('🇾', member=z0diac.user)
                                message = await ctx.message.author.send("to add, p")
                        if reaction33[0].emoji == '🇳':
                            await message.remove_reaction('🇾', member=z0diac.user)
                            message = await ctx.message.author.send("Your umbrella role is... **Third Positioner**. Your subrole is... **National Capitalist**. If you have more questions or a more specific ideology to add, please DM Dakota.")
            if reaction2[0].emoji == '🇳':
                await message_3.remove_reaction('🇾', member=z0diac.user)
                message = await ctx.message.author.send("**Question 2:**\nDo you believe in abolishing the concept of owning private property? (Y for yes, and N for no.)")
                await message.add_reaction('🇾')
                await message.add_reaction('🇳')
                def check(reaction, user):
                    return reaction.count == 2
                reaction4 = await z0diac.wait_for('reaction_add', check=check)
                if reaction4[0].emoji == '🇾':
                    await message.remove_reaction('🇳', member=z0diac.user)
                    message = await ctx.message.author.send( "**Question 3:**\nDo you believe revolution needs to be immediate? (Y for yes, and N for no.)")
                    await message.add_reaction('🇾')
                    await message.add_reaction('🇳')
                    def check(reaction, user):
                        return reaction.count == 2
                    reaction5 = await z0diac.wait_for('reaction_add', check=check)
                    if reaction5[0].emoji == '🇾':
                        await message.remove_reaction('🇳', member=z0diac.user)
                        message = await ctx.message.author.send("Your umbrella role is... **Libertarian Socialist**. Your subrole is... **Anarchocommunist**. If you have more questions or a more specific ideology to add, please DM Dakota.")
                    if reaction5[0].emoji == '🇳':
                        await message.remove_reaction('🇾', member=z0diac.user)
                        message = await ctx.message.author.send("**Question 4:**\nIs revolution by working within the democratic system impossible?")
                        await message.add_reaction('🇾')
                        await message.add_reaction('🇳')
                        def check(reaction, user):
                            return reaction.count == 2
                        reaction5 = await z0diac.wait_for('reaction_add', check=check)
                        if reaction5[0].emoji == '🇾':
                            await message.remove_reaction('🇳', member=z0diac.user)
                            message = await ctx.message.author.send("Your umbrella role is... **Socialist.** Your subrole is... **Marxist** If you have more questions or a more specific ideology to add, please DM Dakota.")
                        if reaction5[0].emoji == '🇳':
                            await message.remove_reaction('🇾', member=z0diac.user)
                            message = await ctx.message.author.send("Your umbrella role is... **Socialist**. Your subrole is... **Democratic Socialist.** If you have more questions or a more specific ideology to add, please DM Dakota.**")
        elif label == "bigdab" or label == "bigDab" or label == "big dab":
            embed = discord.Embed()
            embed.set_author(name="big dab")
            embed.add_field(name="**Type:**", value="Shop Item")
            embed.add_field(name="**Category:**", value="Fun")
            embed.add_field(name="**Price:**", value="2 EP")
            embed.add_field(name="**Status:**", value="TBA")
            embed.add_field(name="**Description:**", value="bigdab is a shop item that allows you to post a full-sized dab instead of a tiny emote.")
            message = await ctx.channel.send(embed=embed)
        elif label == "renamesaldol" or label == "renameSaldol" or label == "rename Saldol":
            embed = discord.Embed()
            embed.set_author(name="Rename Saldol")
            embed.add_field(name="**Type:**", value="Shop Item")
            embed.add_field(name="**Category:**", value="Fun")
            embed.add_field(name="**Price:**", value="5 EP")
            embed.add_field(name="**Status:**", value="Available")
            embed.add_field(name="**Description:**", value="renamesaldol is a shop item that allows you to rename Saldol to whatever you desire; yes, he is not allowed to change whatever you give him. A portion of donated EP goes to him.")
            message = await ctx.channel.send(embed=embed)
        elif label == "membership" or label == "apply" or label == "memberplus":
            embed = discord.Embed()
            embed.set_author(name="Member+ Application")
            embed.add_field(name="**Type:**", value="Shop Item")
            embed.add_field(name="**Category:**", value="Server")
            embed.add_field(name="**Price:**", value="200 EP")
            embed.add_field(name="**Status:**", value="Available")
            embed.add_field(name="**Description:**", value="The membership, AKA Member+, is a shop item that gives you the Member+ role and the ability to apply for a pass to the serious debate channels. If you fail the test, refund is up to the discretion of representatives.")
            message = await ctx.channel.send(embed=embed)
        elif label == "ad" or label == "Ad" or label == "advertisement":
            embed = discord.Embed()
            embed.set_author(name="Advertisement Slot")
            embed.add_field(name="**Type:**", value="Shop Item")
            embed.add_field(name="**Category:**", value="Server")
            embed.add_field(name="**Price:**", value="35 EP")
            embed.add_field(name="**Status:**", value="Available")
            embed.add_field(name="**Description:**", value="The Advertisement Slot is a shop item that allows you to advertise one message on the community billboard channel for everyone to see.")
            message = await ctx.channel.send(embed=embed)
        elif label == "subrole" or label == "Subrole" or label == "sub role":
            embed = discord.Embed()
            embed.set_author(name="Subrole")
            embed.add_field(name="**Type:**", value="Shop Item")
            embed.add_field(name="**Category:**", value="Server")
            embed.add_field(name="**Price:**", value="70 EP")
            embed.add_field(name="**Status:**", value="Available")
            embed.add_field(name="**Description:**", value="subrole is a shop item that gives you a role to tag yourself with.")
            message = await ctx.channel.send(embed=embed)
        elif label == "topic":
            embed = discord.Embed()
            embed.set_author(name="Topic")
            embed.add_field(name="**Type:**", value="Shop Item")
            embed.add_field(name="**Category:**", value="Server")
            embed.add_field(name="**Price:**", value="7 EP")
            embed.add_field(name="**Status:**", value="Available")
            embed.add_field(name="**Description:**", value="Topic is a command that allows you to suggest topics for upcoming podcasts; topics can be server, technology, politics, philosophy, or gaming related.")
            message = await ctx.channel.send(embed=embed)
        elif label == "omegadebate":
            embed = discord.Embed()
            embed.set_author(name="Omega Debate")
            embed.add_field(name="**Type:**", value="Shop Item")
            embed.add_field(name="**Category:**", value="Server")
            embed.add_field(name="**Price:**", value="2 DP per message")
            embed.add_field(name="**Status:**", value="TBA")
            embed.add_field(name="**Description:**", value="Omega Debate is a channel where each message you send is taxed with 2 DP, forcing you to use your messages wisely. Getting a message pinned by a representative will net you 10 EP.")
            message = await ctx.channel.send(embed=embed)
        elif label == "jobs":
            embed = discord.Embed()
            embed.set_author(name="Job Postings")
            embed.add_field(name="**Contributor:**", value="The fastest way to earn EP. Write quality messages that get pinned, do filibusters and formal debates. This will also reflect on your record, increasing the chances of your serious-debate application getting accepted.")
            embed.add_field(name="**Developer:**", value="Work on developing the Reaganator 3000. Get paid in EP for each commit and be able to play a part in the structural development of the server.")
            embed.add_field(name="**Podcast:**", value="Be a guest or assistant on the weekly PWH podcast, and get paid in EP each week you're present.")
            embed.add_field(name="**Legislator:**", value="Challenge your incumbent Co-Governor to a special election, and if you win, you'll be able to work on managing your wing channels and get paid per vote/bill created.")
            embed.add_field(name="**Private Attorney:**", value="Take on cases and get paid by your client for your efforts.")
            embed.add_field(name="**Volunteer:**", value="Help out people who need help in #personal-help; you must be able to demonstrate your ability, but you will be paid in EP by the server depending on client satisfaction.")
            message = await ctx.channel.send(embed=embed)
        elif label == "channels":
            embed = discord.Embed()
            embed.set_author(name="Channels")
            embed.add_field(name="**Omega Debate**", value="omega-debate is the main channel, where your ability to discuss is purposefully limited by your Daily Points, which is reset to 144 every day. Each message costs 2 DP, so talk wisely. If you run out before the day is done, you can trade your EP for DP with another user or wait until the day is done.")
            embed.add_field(name="**Peanut Gallery:**", value=" peanut-gallery is the second of the default channels, where people comment on filibusters, podcasts, court cases, legislative proceedings, and formal debates. Any other discussion is strictly prohibited but there is no statute of limitations on what you can discuss.")
            embed.add_field(name="**Serious Debate**", value="serious-debate is much more topical and in-depth. Memeing, emojis, strawmen, mocking other's viewpoints without substance, one-liners, and blanket claims are absolutely not allowed and hinder the quality of discussion. This is more strictly moderated, however, you are free to discuss any topic. You gain access to here by participating in the other debate channels, and having high quality discussion. 200 EP plus approval from the council nets you into this channel.")
            embed.add_field(name="**Formal Debate:**", value="formal-debate is a structured debate format for professional style debating. Do /debate [MEMBER] [TOPIC] to debate them. ")
            embed.add_field(name="**Filibusters:**", value="filibusters  is the area for you to explain a complex topic without interruptions, and to get your point across or educate someone on a topic.")
            embed.add_field(name="**Podcast:**", value="The podcast, run by @ The Firebird, is a weekly stream that discusses various issues proposed by the PWH community.")
            message = await ctx.channel.send(embed=embed)
        elif label == "B-1001":
            embed = discord.Embed()
            embed.set_author(name="B-0001: The Compact Council Act", icon_url='https://www.emojibase.com/resources/img/emojis/hangouts/1f4c3.png',url='https://docs.google.com/document/d/12UKv2uy8LG-AIGw6QhrZ8TzhGcrZg7CgjzECWy4ZcXs/edit')
            embed.add_field(name="**Proposed By:**", value="Dakota")
            embed.add_field(name="**Proposed On:**", value="3/31/2018")
            embed.add_field(name="**Provisions:**", value="8")
            embed.add_field(name="**Provisions Passed:**", value="8")
            embed.add_field(name="**Summary:**", value="A bill designed with the sole purpose of shrinking down the council's size to improve efficiency.")
            message = await ctx.channel.send(embed=embed)
        elif label == "B-1002":
            embed = discord.Embed()
            embed.set_author(name="B-0002: The Dustpan Bill",icon_url='https://www.emojibase.com/resources/img/emojis/hangouts/1f4c3.png',url='https://docs.google.com/document/d/1lyhyEnln3etE4i6YfXXyFLV-Xc5TD-8VYkoxOHXGdqE/edit')
            embed.add_field(name="**Proposed By:**", value="Dakota")
            embed.add_field(name="**Proposed On:**", value="4/3/2018")
            embed.add_field(name="**Provisions:**", value="7")
            embed.add_field(name="**Provisions Passed:**", value="6")
            embed.add_field(name="**Summary:**", value="An omnibus bill intended to clean up the side-effects of B-0001.")
            message = await ctx.channel.send(embed=embed)
        elif label == "B-1003":
            embed = discord.Embed()
            embed.set_author(name="B-0003: The Quality Discussion Act",icon_url='https://www.emojibase.com/resources/img/emojis/hangouts/1f4c3.png',url='https://docs.google.com/document/d/1a81hF-H9TzpE5KnTVtgH5CTfdtj7NVER0g0hznxL3Co/edit')
            embed.add_field(name="**Proposed By:**", value="Dakota")
            embed.add_field(name="**Proposed On:**", value="4/25/2018")
            embed.add_field(name="**Provisions:**", value="7")
            embed.add_field(name="**Provisions Passed:**", value="0")
            embed.add_field(name="**Summary:**", value="A bill designed to return quality back to discussion. Was shelved indefinitely, but served as basis for the Economy Update.")
            message = await ctx.channel.send(embed=embed)
        elif label == "E-1488":
            embed = discord.Embed()
            embed.set_author(name="E-1488: Nazi Defense Motion",icon_url='http://www.emoji.co.uk/files/phantom-open-emojis/objects-phantom/12926-lower-left-fountain-pen.png',url='https://docs.google.com/document/d/1Q-_oJPH11DXCrnEElr5VUCq4snonOIFcADyRjz1pCYY/edit')
            embed.add_field(name="**Issued By:**", value="Dakota")
            embed.add_field(name="**Proposed On:**", value="4/2/2018")
            embed.add_field(name="**Status:**", value="Overturned")
            embed.add_field(name="**Summary:**", value="An executive order suspending due process for certain individuals following a Nazi raid.")
            message = await ctx.channel.send(embed=embed)
        elif label == "E-2000":
            embed = discord.Embed()
            embed.set_author(name="E-2000: The Economy Update",icon_url='http://www.emoji.co.uk/files/phantom-open-emojis/objects-phantom/12926-lower-left-fountain-pen.png',url='https://docs.google.com/document/d/1znVidkfu08pye-n6ZMiCiKiuo-DAGqmnBEt5u4j7r5I/edit?usp=sharing')
            embed.add_field(name="**Issued By:**", value="Dakota")
            embed.add_field(name="**Proposed On:**", value="5/29/2018")
            embed.add_field(name="**Status:**", value="Active")
            embed.add_field(name="**Summary:**", value="An executive order restoring discussion quality through a government overhaul and introduction of an economy.")
            message = await ctx.channel.send(embed=embed)
        elif label == "J-1001":
            embed = discord.Embed()
            embed.set_author(name="J-1001: Gunnz101 v. PaxBritannicus",icon_url='http://icons.iconarchive.com/icons/iconleak/or/256/auction-hammer-icon.png',url='https://docs.google.com/document/d/1Zctkzht7niHCJmqGkktIXoA3v8HQj4Dq1wiPkHcQM6o/edit')
            embed.add_field(name="**Plantiff:**", value="Gunnz101")
            embed.add_field(name="**Defendant:**", value="PaxBritannicus")
            embed.add_field(name="**Prosecutor:**", value="Auren")
            embed.add_field(name="**Defense:**", value="Cezar")
            embed.add_field(name="**Trial Date:**", value="3/29/2018")
            embed.add_field(name="**Verdict:**", value="Pax was found guilty of violating Rules 1 and 7.")
            message = await ctx.channel.send(embed=embed)
        elif label == "J-1002":
            embed = discord.Embed()
            embed.set_author(name="J-1002: sparkle v. Cezar and Oxenfree", icon_url='http://icons.iconarchive.com/icons/iconleak/or/256/auction-hammer-icon.png', url='https://docs.google.com/document/d/1VCLOyWswz8XYm5I0slE0Aos1nP2ZHVSrEdVsDpHweBE/edit')
            embed.add_field(name="**Plantiff:**", value="Gunnz101")
            embed.add_field(name="**Defendant:**", value="PaxBritannicus")
            embed.add_field(name="**Prosecutor:**", value="Auren")
            embed.add_field(name="**Defense:**", value="Cezar")
            embed.add_field(name="**Trial Date:**", value="4/2/2018")
            embed.add_field(name="**Verdict:**", value="Cezar was found innocent, Oxen decided to plead guilty.")
            message = await ctx.channel.send(embed=embed)
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
    if reacter != z0diac.user.id:
        roles = z0diac.get_channel(channel).guild.roles
        umbrella_roles = [discord.utils.get(roles, id=420735827023495169), discord.utils.get(roles, id=443242847681118218), discord.utils.get(roles, id=381178125591117827),discord.utils.get(roles, id=382557327892676619), discord.utils.get(roles, id=420735827023495169), discord.utils.get(roles, id=381176934131957760), discord.utils.get(roles, id=381177002033676298), discord.utils.get(roles, id=409124661272641536), discord.utils.get(roles, id=381176967631863810), discord.utils.get(roles, id=448633320431943682), discord.utils.get(roles, id=381177029464293386), discord.utils.get(roles, id=427819576882102273), discord.utils.get(roles, id=381177107616759810), discord.utils.get(roles, id=416369684179320834), discord.utils.get(roles, id=424645022927945736), discord.utils.get(roles, id=409483695582478348)]
        if 451558008787566593 == message:
            setserver = set(umbrella_roles)
            setuser = set(discord.utils.get(z0diac.get_all_members(), id=reacter).roles)
            try:
                await z0diac.get_guild(381170494814289922).get_member(reacter).remove_roles(next(iter(setuser.intersection(setserver))))
            except:
                pass
            if str(reaction) == '<:socialist:454666012860743695>':
                await z0diac.get_guild(381170494814289922).get_member(reacter).add_roles(discord.utils.get(z0diac.get_guild(381170494814289922).roles, id=443242847681118218))
                await discord.utils.get(z0diac.get_all_members(), id=reacter).send('You have been given the ' + discord.utils.get(z0diac.get_guild(381170494814289922).roles, id=443242847681118218).name + ' role.')
            elif str(reaction) == '<:social_democrat:454666536142110721>':
                await z0diac.get_guild(381170494814289922).get_member(reacter).add_roles(discord.utils.get(z0diac.get_guild(381170494814289922).roles, id=381178125591117827))
                await z0diac.get_guild(381170494814289922).get_member(reacter).send('You have been given the ' + discord.utils.get(z0diac.get_guild(381170494814289922).roles, id=381178125591117827).name + ' role.')
            elif str(reaction) == '<:libertarian_socialist:454663573386559499>':
                await z0diac.get_guild(381170494814289922).get_member(reacter).add_roles(discord.utils.get(z0diac.get_guild(381170494814289922).roles, id=382557327892676619))
                await z0diac.get_guild(381170494814289922).get_member(reacter).send('You have been given the ' + discord.utils.get(z0diac.get_guild(381170494814289922).roles, id=382557327892676619).name + ' role.')
            elif str(reaction) == '<:green:454664511173951494>':
                await z0diac.get_guild(381170494814289922).get_member(reacter).add_roles(discord.utils.get(z0diac.get_guild(381170494814289922).roles, id=420735827023495169))
                await z0diac.get_guild(381170494814289922).get_member(reacter).send('You have been given the ' + discord.utils.get(z0diac.get_guild(381170494814289922).roles, id=420735827023495169).name + ' role.')
        elif 451558090727358495 == message:
            setserver = set(umbrella_roles)
            setuser = set(discord.utils.get(z0diac.get_all_members(), id=reacter).roles)
            try:
                await z0diac.get_guild(381170494814289922).get_member(reacter).remove_roles(next(iter(setuser.intersection(setserver))))
            except:
                pass
            if str(reaction) == '<:centrist:454666611568410634>':
                combinedset = [umbrella_roles + discord.utils.get(z0diac.get_all_members(), id=reacter).roles]
                await z0diac.get_guild(381170494814289922).get_member(reacter).add_roles(discord.utils.get(z0diac.get_guild(381170494814289922).roles, id=381176934131957760))
                await discord.utils.get(z0diac.get_all_members(), id=reacter).send('You have been given the ' + discord.utils.get(z0diac.get_guild(381170494814289922).roles, id=381176934131957760).name + ' role.')
            elif str(reaction) == '<:neoliberal:454666880771424258>':
                await z0diac.get_guild(381170494814289922).get_member(reacter).add_roles(discord.utils.get(z0diac.get_guild(381170494814289922).roles, id=381177002033676298))
                await z0diac.get_guild(381170494814289922).get_member(reacter).send('You have been given the ' + discord.utils.get(z0diac.get_guild(381170494814289922).roles, id=381177002033676298).name + ' role.')
            elif str(reaction) == '<:neoconservative:454664747464392724>':
                await z0diac.get_guild(381170494814289922).get_member(reacter).add_roles(discord.utils.get(z0diac.get_guild(381170494814289922).roles, id=381176967631863810))
                await z0diac.get_guild(381170494814289922).get_member(reacter).send('You have been given the ' + discord.utils.get(z0diac.get_guild(381170494814289922).roles, id=381176967631863810).name + ' role.')
            elif str(reaction) == '<:classical_liberal:454665209009668097>':
                await z0diac.get_guild(381170494814289922).get_member(reacter).add_roles(discord.utils.get(z0diac.get_guild(381170494814289922).roles, id=381177029464293386))
                await z0diac.get_guild(381170494814289922).get_member(reacter).send('You have been given the ' + discord.utils.get(z0diac.get_guild(381170494814289922).roles, id=381177029464293386).name + ' role.')
            elif str(reaction) == '<:libertarian:454664092305588235>':
                await z0diac.get_guild(381170494814289922).get_member(reacter).add_roles(discord.utils.get(z0diac.get_guild(381170494814289922).roles, id=381177107616759810))
                await z0diac.get_guild(381170494814289922).get_member(reacter).send('You have been given the ' + discord.utils.get(z0diac.get_guild(381170494814289922).roles, id=381177107616759810).name + ' role.')
        elif 451558134784196611 == message:
            setserver = set(umbrella_roles)
            setuser = set(discord.utils.get(z0diac.get_all_members(), id=reacter).roles)
            try:
                await z0diac.get_guild(381170494814289922).get_member(reacter).remove_roles(next(iter(setuser.intersection(setserver))))
            except:
                pass
            if str(reaction) == '<:nationalist:454663855809757195>':
                await z0diac.get_guild(381170494814289922).get_member(reacter).add_roles(discord.utils.get(z0diac.get_guild(381170494814289922).roles, id=427819576882102273))
                await discord.utils.get(z0diac.get_all_members(), id=reacter).send('You have been given the ' + discord.utils.get(z0diac.get_guild(381170494814289922).roles, id=427819576882102273).name + ' role.')
            elif str(reaction) == '<:paternalist:454663251633111050>':
                await z0diac.get_guild(381170494814289922).get_member(reacter).add_roles(discord.utils.get(z0diac.get_guild(381170494814289922).roles, id=416369684179320834))
                await z0diac.get_guild(381170494814289922).get_member(reacter).send('You have been given the ' + discord.utils.get(z0diac.get_guild(381170494814289922).roles, id=416369684179320834).name + ' role.')
            elif str(reaction) == '<:paleoconservative:454662578488999937>':
                await z0diac.get_guild(381170494814289922).get_member(reacter).add_roles(discord.utils.get(z0diac.get_guild(381170494814289922).roles, id=424645022927945736))
                await z0diac.get_guild(381170494814289922).get_member(reacter).send('You have been given the ' + discord.utils.get(z0diac.get_guild(381170494814289922).roles, id=424645022927945736).name + ' role.')
            elif str(reaction) == '<:theologue:454667115601854474>':
                await z0diac.get_guild(381170494814289922).get_member(reacter).add_roles(roles, id=409124661272641536)
                await z0diac.get_guild(381170494814289922).get_member(reacter).send('You have been given the ' + discord.utils.get(z0diac.get_guild(381170494814289922).roles, id=409124661272641536).name + ' role.')
            elif str(reaction) == '<:third_positioner:454665463847321602>':
                await z0diac.get_guild(381170494814289922).get_member(reacter).add_roles(discord.utils.get(z0diac.get_guild(381170494814289922).roles, id=448633320431943682))
                await z0diac.get_guild(381170494814289922).get_member(reacter).send('You have been given the ' + discord.utils.get(z0diac.get_guild(381170494814289922).roles, id=448633320431943682).name + ' role.')
        elif 451558174965760000 == message:
            setserver = set(umbrella_roles)
            setuser = set(discord.utils.get(z0diac.get_all_members(), id=reacter).roles)
            try:
                await z0diac.get_guild(381170494814289922).get_member(reacter).remove_roles(next(iter(setuser.intersection(setserver))))
            except:
                pass
            if str(reaction) == '<:apolitical:448485954462679060>':
                await z0diac.get_guild(381170494814289922).get_member(reacter).add_roles(discord.utils.get(z0diac.get_guild(381170494814289922).roles,id=409483695582478348))
                await z0diac.get_guild(381170494814289922).get_member(reacter).send('You have been given the Apolitical role.')
        elif str(reaction) == '📌' or str(reaction) == '📍':
            with open("dictionary.json", 'r+') as f:
                    if channel == 450415484832186369:
                        if discord.utils.get(z0diac.get_guild(381170494814289922).roles, id=448291958582935562) in z0diac.get_guild(381170494814289922).get_member(reacter).roles or reacter == 176160436331216896:
                            with open("dictionary.json", 'r+') as f:
                                x = await discord.utils.get(z0diac.get_all_channels(), id=channel).get_message(message)
                                repkey = json.load(f)
                                currentvalue_customer = repkey.get(str(x.author.id))
                                dollar_amount = 10
                                repkey[str(x.author.id)] = currentvalue_customer + dollar_amount
                                f.seek(0)
                                json.dump(repkey, f)
                                f.truncate()
                                weee = await discord.utils.get(z0diac.get_all_channels(), id=channel).get_message(message)
                                www = weee.reactions[0].count
                                if www <= 1:
                                    x = await discord.utils.get(z0diac.get_all_channels(), id=channel).get_message(message)
                                    embed = discord.Embed(title=("On: " + x.created_at.strftime("%Y-%m-%d %H:%M:%S") + " in #" + x.channel.name), color=x.author.color, description=x.content)
                                    embed.set_author(name=x.author.name, icon_url=x.author.avatar_url)
                                    msg = await z0diac.get_channel(450720964028923905).send(embed=embed)
                    elif z0diac.get_channel(446400765775314947):
                        print(channel)
                        weee = await discord.utils.get(z0diac.get_all_channels(), id=channel).get_message(message)
                        www = weee.reactions[0].count
                        if www <= 1:
                            x = await discord.utils.get(z0diac.get_all_channels(), id=channel).get_message(message)
                            embed = discord.Embed(title=("On: " + x.created_at.strftime("%Y-%m-%d %H:%M:%S") + " in #" + x.channel.name), color=x.author.color, description=x.content)
                            embed.set_author(name=x.author.name,icon_url=x.author.avatar_url)
                            msg = await z0diac.get_channel(446400765775314947).send(embed=embed)




@z0diac.command()
async def buy(ctx):
    with open("dictionary.json", 'r+') as f:
        repkey = json.load(f)
        currentvalue_customer = repkey.get(str(ctx.message.author.id))
        if ctx.channel != z0diac.get_channel(450415484832186369):
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
                        await ctx.channel.send('You need 2 EP to do that!')
            elif ctx.message.content[5:13] == 'dmsaldol':
                    dollar_amount = 10
                    if currentvalue_customer - dollar_amount >= 0:
                        repkey[str(ctx.message.author.id)] = currentvalue_customer - dollar_amount
                        f.seek(0)
                        json.dump(repkey, f)
                        f.truncate()
                        await ctx.guild.get_member(173451290268008448).send('An anonymous user wants to tell you: ' + ctx.message.content[14:])
                        await ctx.message.delete()
                        await ctx.message.author.send('Your DM was sent.')
                    else:
                        await ctx.channel.send('You need 2 EP to do that!')
            elif ctx.message.content[5:16] == 'renamebulba':
                if ctx.message.author != discord.utils.get(ctx.guild.members, id=263014410015080459):
                    saldol = ctx.guild.get_member(263014410015080459)
                    saldolname = saldol.display_name
                    dollar_amount = 10
                    if currentvalue_customer - dollar_amount >= 0:
                            repkey[str(ctx.message.author.id)] = currentvalue_customer - dollar_amount
                            f.seek(0)
                            json.dump(repkey, f)
                            f.truncate()
                    try:
                        await saldol.edit(nick=ctx.message.content[17:])
                        await ctx.channel.trigger_typing()
                        time.sleep(3)
                        aftersaldol = saldol.display_name
                        await ctx.channel.send(saldolname + ', more like ' + aftersaldol + '!')
                        f.seek(0)
                        json.dump(repkey, f)
                        f.truncate()
                    except discord.ext.commands.errors.CommandInvokeError:
                        await ctx.channel.send("Too long.")
                else:
                    await ctx.channel.send("Nice try, Saldol.")
            elif ctx.message.content[5:12] == 'subrole':
                dollar_amount = 70
                if currentvalue_customer - dollar_amount >= 0:
                    repkey[str(ctx.message.author.id)] = currentvalue_customer - dollar_amount
                    f.seek(0)
                    json.dump(repkey, f)
                    f.truncate()
                    role_name = await ctx.guild.create_role(name=ctx.message.content[12:],mentionable=True)
                    await ctx.message.author.add_roles(role_name)
                    await ctx.channel.send('You have been given the' + ctx.message.content[12:] + ' role.')
                else:
                    await ctx.channel.send('You need 70 EP to do that!')
            elif ctx.message.content[5:15] == 'memberplus':
                dollar_amount = 200
                print('Pass')
                if currentvalue_customer - dollar_amount >= 0:
                    repkey[str(ctx.message.author.id)] = currentvalue_customer - dollar_amount
                    f.seek(0)
                    json.dump(repkey, f)
                    f.truncate()
                    await ctx.message.author.add_roles(discord.utils.get(ctx.guild.roles,id=450414068742750208))
                    await z0diac.get_channel(450476263270776842).send("<@&433012201423634442>, please vet " + ctx.message.author.display_name + " in this channel. If you have any questions with the process, PM Dakota.")
                else:
                   await ctx.message.author.send('You cannot afford that!')
            elif ctx.message.content[5:10] == 'topic':
                check = commands.has_role(discord.utils.get(ctx.guild.roles, id=448902429275324427))
                if check is True:
                    dollar_amount = 0
                else:
                    dollar_amount = 15
                if currentvalue_customer - dollar_amount >= 0:
                    repkey[str(ctx.message.author.id)] = currentvalue_customer - dollar_amount
                    f.seek(0)
                    json.dump(repkey, f)
                    f.truncate()
                embed = discord.Embed(title=(ctx.message.author.display_name + " (" + ctx.message.created_at.strftime("%Y-%m-%d %H:%M:%S") + ")"), color=ctx.message.author.color, description=ctx.message.content[11:])
                embed.set_thumbnail(url=ctx.message.author.avatar_url)
                message = await z0diac.get_channel(448905798509264906).send(embed=embed)
                await message.add_reaction('✅')
                await message.add_reaction('❎')
                await ctx.message.delete()
                await ctx.message.author.send('Your suggestion has been sent.')
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
                                    repkey[str(ctx.message.author.id)] = (currentvalue_giver - int(ctx.message.content[dollar_amount:]))
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
            elif ctx.message.content[5:11] == 'dpgift':
                try:
                    with open("dp.json", 'r+') as f:
                        repkey = json.load(f)
                        currentvalue_recipient = repkey.get(str(ctx.message.raw_mentions[0]))
                        currentvalue_giver = repkey.get(str(ctx.message.author.id))
                        dollar_amount = ctx.message.content.find('>') + 1
                        if ctx.message.raw_mentions[0] != ctx.message.author.id:
                            if currentvalue_giver - int(ctx.message.content[dollar_amount:]) >= 0:
                                if int(ctx.message.content[dollar_amount:]) > 0:
                                    repkey[str(ctx.message.author.id)] = (currentvalue_giver - int(ctx.message.content[dollar_amount:]))
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
                                    await ctx.channel.send( 'You have successfully gifted ' + (str(ctx.message.mentions[0]))[:-5] + payment + ' Daily Points.')
                                else:
                                    await ctx.channel.send('Gifts must be a positive number, nice try.')
                            else:
                                print('You cannot afford that!')
                        else:
                            await ctx.channel.send("Nice try, but you can't give yourself cash.")
                except IndexError or ValueError:
                    await ctx.channel.send('Something went wrong, remember to format your message as: /buy dpgift [mentioned person] [number].')
                    traceback.print_exc()


@z0diac.command()
async def vote(ctx):
    if ctx.message.content[6:12] == 'speaker':
        if discord.utils.get(ctx.guild.roles, id=416369684179320834) in ctx.message.author.roles or discord.utils.get(ctx.guild.roles, id=443242847681118218) in ctx.message.author.roles or discord.utils.get(ctx.guild.roles, id=443242847681118218) in ctx.message.author.roles or discord.utils.get(ctx.guild.roles, id=420735827023495169) in ctx.message.author.roles or discord.utils.get(ctx.guild.roles, id=382557327892676619) in ctx.message.author.roles or discord.utils.get(ctx.guild.roles, id=381178125591117827) in ctx.message.author.roles:
            await ctx.message.channel.send('Mention who would you like to vote for for speaker:\nBladeHoldin - Libertarian Socialist\nThe Firebird - Green\nBearTheIndependent - Social Democrat\nTsarNicky - Paternalist')


@z0diac.command()
async def optinlounge(ctx):
    await ctx.message.author.add_roles(discord.utils.get(ctx.guild.roles,id=447429561366478849))
    await ctx.message.author.send('You have been opted into lounge!')

@z0diac.event
async def on_message(message):
    if message.channel == z0diac.get_channel(450415484832186369):
        with open("dp.json", 'r+') as f:
            repkey = json.load(f)
            currentvalue_customer = repkey.get(str(message.author.id))
            if currentvalue_customer == 50 or currentvalue_customer == 25:
                await message.author.send("You're down to " + str(currentvalue_customer) + " DP. Either conserve your remaining DP by being more thorough in your messages or trade your EP to another player for DP.")
            dollar_amount = 2
            if currentvalue_customer - dollar_amount >= 0:
                repkey[str(message.author.id)] = currentvalue_customer - dollar_amount
                f.seek(0)
                json.dump(repkey, f)
                f.truncate()
            else:
                await message.delete()
                await message.author.send('You ran out of Daily Points. Your Daily points will refill tomorrow, but you can earn more trading your EP for DP with other members. Do `/whatis earnEP` to find out more.')
    await z0diac.process_commands(message)


@z0diac.command()
async def refill(ctx):
    if ctx.message.author.id == 176160436331216896:
        with open("dp.json", "r+") as f:
            dpkey = json.load(f)
            keys = list(dpkey.keys())
            for x in keys:
                print(x)
                dpkey[x] = 100
                f.seek(0)
                json.dump(dpkey, f)
                f.truncate()
        await ctx.message.channel.send("You have successfully refilled everyone's Daily Points")


@z0diac.command()
async def filibuster(ctx):
    if len((discord.utils.get(ctx.guild.roles, id=450796233192243210)).members) == 0:
        await ctx.message.author.add_roles(discord.utils.get(ctx.guild.roles, id=450796233192243210))
        await ctx.guild.get_channel(414876520541192203).send(ctx.message.author.mention + ' will be speaking on the following topic: ' + ctx.message.content[12:] + "Once you are done speaking, do /conclude to exit the filibuster.")
        await ctx.guild.get_channel(448904930787459080).set_permissions(ctx.guild.default_role, send_messages=None)
        await ctx.guild.get_channel(448904930787459080).send('A filibuster event is beginning, join us! To learn more about events, do `/whatis channels`!')
    else:
        await ctx.message.author.send('Someone is currently filibustering. Please wait until they are done. If you believe this is an error, please DM Dakota.')

@z0diac.command()
async def conclude(ctx):
    if discord.utils.get(ctx.guild.roles, id=450796233192243210) in ctx.message.author.roles:
        await ctx.message.delete()
        await ctx.message.author.remove_roles(discord.utils.get(ctx.guild.roles, id=450796233192243210))
        msg = await z0diac.get_channel(414876520541192203).send(ctx.message.author.mention + ' has concluded their filibuster. Please react to this message with an applause emoji if you felt it was a solid contribution. They will recieve EP at no cost to you if you do choose to clap.')
        await msg.add_reaction('👏')
        await ctx.guild.get_channel(448904930787459080).set_permissions(ctx.guild.default_role, send_messages=False)
        await ctx.guild.get_channel(448904930787459080).send('Thank you for joining us during the filibuster! Please tune in next time! To learn more about events, do `/whatis channels`!')
    else:
        await ctx.message.author.send('You cannot do that.')

@z0diac.command()
async def trade(ctx):
    await ctx.message.author.send("How much EP are you willing to spend? (Please only reply with a number)")
    def check(m):
        try:
            ep_spend = int(m.content)
            return type(ep_spend) == int
        except:
            ctx.message.author.send('That is not a number.')
            return False
    epspend = await z0diac.wait_for('message', check=check)
    await ctx.message.author.send("How much DP do you expect in exchange? (Please only reply with a number)")
    def check(m):
        try:
            dp_get = int(m.content)
            return type(dp_get) == int
        except:
            ctx.message.author.send('That is not a number.')
    dpget = await z0diac.wait_for('message', check=check)
    with open("dictionary.json", 'r+') as f:
        repkey = json.load(f)
        currentvalue_customer = repkey.get(str(epspend.author.id))
        dollar_amount = int(epspend.content)
        if currentvalue_customer - dollar_amount >= 0:
            embed = discord.Embed(title='Trade')
            embed.set_author(name=epspend.author, icon_url=epspend.author.avatar_url)
            embed.add_field(name="**Offer:**", value=(epspend.content + " EP"))
            embed.add_field(name="**Wants:**", value=(dpget.content + " DP"))
            message = await ctx.guild.get_channel(447424864907689984).send(embed=embed)
            with open("dp.json", 'r+') as f:
                repkey = json.load(f)
                await message.add_reaction('✅')
                dollar_amount = int(dpget.content)
                def check(r,user):
                    print(user)
                    print(user.id)
                    return r.message.id == message.id and str(user) != 'zodiac-bot#0559' and (repkey.get(str(user.id)) - dollar_amount) >= 0
                reactio = await z0diac.wait_for('reaction_add',check=check)
                print(reactio)
                reactiouser = reactio[1]
                await reactiouser.send("You have completed the trade.")
                await epspend.author.send("You have completed the trade.")
                await message.delete()
                print(epspend.author.id)
                currentvalue_seller = repkey.get(str(reactiouser.id))
                repkey[str(reactiouser.id)] = currentvalue_seller + dollar_amount
                repkey[str(epspend.author.id)] = currentvalue_customer - dollar_amount
                f.seek(0)
                json.dump(repkey, f)
                f.truncate()
                with open("dp.json", 'r+') as f:
                    repkey = json.load(f)
                    dollar_amount = int(dpget.content)
                    if currentvalue_seller - dollar_amount >= 0:
                        currentvalue_seller = repkey.get(str(reactiouser.id))
                        repkey[str(reactiouser.id)] = currentvalue_seller - dollar_amount
                        repkey[str(epspend.author.id)] = currentvalue_customer + dollar_amount
                        f.seek(0)
                        json.dump(repkey, f)
                        f.truncate()



@z0diac.command()
async def arrest(ctx):
    await ctx.message.delete()
    if ctx.message.author == ctx.guild.get_member(176160436331216896) or discord.utils.get(ctx.guild.roles,id=429705375848202240) in ctx.message.author.roles:
        for x in ctx.message.mentions[0].roles:
            await ctx.message.mentions[0].remove_roles(discord.utils.get(ctx.guild.roles,id=x.id))
        await ctx.message.mentions[0].add_roles(discord.utils.get(ctx.guild.roles,id=400016622498349057))
        await ctx.message.mentions[0].send('You have been jailed. You will be unable to speak until then. Please go to your respective wing court, and ping your lawyer by doing @Lawyer in that channel. If there is any questions, DM Dakota.')

@z0diac.command()
async def peanut(ctx):
    if ctx.message.author.id == 176160436331216896:
        if ctx.message.content[8:] == 'close':
           await ctx.guild.get_channel(448904930787459080).set_permissions(ctx.guild.default_role, send_messages=False)
           await ctx.guild.get_channel(448904930787459080).send('Thank you for joining us during the event! Please tune in next time! To learn more about events, do `/whatis event`!')
           await ctx.message.delete
        if ctx.message.content[8:] == 'open':
           await ctx.guild.get_channel(448904930787459080).set_permissions(ctx.guild.default_role, send_messages=None)
           await ctx.guild.get_channel(448904930787459080).send('An event is beginning, join us! To learn more about events, do `/whatis event`!')
           await ctx.message.delete





z0diac.run("MzgzMzg1MTk4NTM0MDY2MTg3.Df75Pg.aDpmWPPsoXJORinQlcWHoCdJQdc")

