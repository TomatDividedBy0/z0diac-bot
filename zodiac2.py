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
            embed.set_author(name="Socialist",icon_url=z0diac.get_emoji(448477016430215169).url)
            embed.add_field(name="**Type:**", value="Umbrella Role")
            embed.add_field(name="**Wing:**", value="Left")
            embed.add_field(name="**Representative:**", value="sparkle#5001")
            embed.add_field(name="**Members:**", value=str(len(discord.utils.get(ctx.guild.roles,id=443242847681118218).members)))
            embed.add_field(name="**Description:**", value="Socialists believe in the public ownership of the means of production. They are commonly found on the far-left end of the compass, with varying degrees of authoritarianism/libertarianism.")
            message = await ctx.channel.send(embed=embed)
        elif label == "Classical Liberal" or label == "classical liberal" or label == "classical lib" or label == "Classical liberal" or label == "Classical Lib" or label == "Classical lib":
            embed = discord.Embed(color=discord.utils.get(ctx.guild.roles,id=381177029464293386).color)
            embed.set_author(name="Classical Liberal",icon_url=z0diac.get_emoji(448478811076427786).url)
            embed.add_field(name="**Type:**", value="Umbrella Role")
            embed.add_field(name="**Wing:**", value="Right")
            embed.add_field(name="**Representative:**", value="Revolt#8500")
            embed.add_field(name="**Members:**", value=str(len(discord.utils.get(ctx.guild.roles,id=381177029464293386).members)))
            embed.add_field(name="**Description:**", value="Classical liberals adhere strongly to the rights of the individual, however, unlike libertarians, they are a lot more moderate on the free market. You'll usually find them straight down from center or near center.")
            message = await ctx.channel.send(embed=embed)
        elif label == "Nationalist" or label == "nationalist":
            embed = discord.Embed(color=discord.utils.get(ctx.guild.roles, id=427819576882102273).color)
            embed.set_author(name="Nationalist", icon_url=z0diac.get_emoji(448478321743888406).url)
            embed.add_field(name="**Type:**", value="Umbrella Role")
            embed.add_field(name="**Wing:**", value="Right")
            embed.add_field(name="**Representative:**", value="Gunnz011#7212")
            embed.add_field(name="**Members:**", value=str(len(discord.utils.get(ctx.guild.roles, id=427819576882102273).members)))
            embed.add_field(name="**Description:**", value="Nationalists believe in putting their own country or group first above others. They are often protectionist, and come in many different variants from Civic Nationalists to Ethnonationalists.")
            message = await ctx.channel.send(embed=embed)
        elif label == "Right Libertarian" or label == "Libertarian" or label == "libertarian" or label == "right libertarian":
            embed = discord.Embed(color=discord.utils.get(ctx.guild.roles, id=381177107616759810).color)
            embed.set_author(name="Libertarian", icon_url=z0diac.get_emoji(448478542444101643).url)
            embed.add_field(name="**Type:**", value="Umbrella Role")
            embed.add_field(name="**Wing:**", value="Right")
            embed.add_field(name="**Representative:**", value="BulbaBlin#7776")
            embed.add_field(name="**Members:**", value=str(len(discord.utils.get(ctx.guild.roles, id=381177107616759810).members)))
            embed.add_field(name="**Description:**", value="Libertarians tend to favor solutions that involve the free market and the individual over government intervention, detesting excess public spending and tax hikes. They are found everywhere on the bottom right of the compass.")
            message = await ctx.channel.send(embed=embed)
        elif label == "Paleoconservative" or label == "paleocon" or label == "paleoconservative" or label == "paleocon":
            embed = discord.Embed(color=discord.utils.get(ctx.guild.roles, id=424645022927945736).color)
            embed.set_author(name="Paleoconservative", icon_url=z0diac.get_emoji(448478006747332608).url)
            embed.add_field(name="**Type:**", value="Umbrella Role")
            embed.add_field(name="**Wing:**", value="Right")
            embed.add_field(name="**Representative:**", value="saldol-1104#5500")
            embed.add_field(name="**Members:**", value=str(len(discord.utils.get(ctx.guild.roles, id=424645022927945736).members)))
            embed.add_field(name="**Description:**", value="Paleoconservatives, also known as the Old Right, date back to the early 20th century in their beliefs. They place social tradition and economic nonintervention above all else, often being in the top right of the compass.")
            message = await ctx.channel.send(embed=embed)
        elif label == "LibtSoc" or label == "Libertarian Socialist" or label == "Libertarian Socialist" or label == "libertarian socialist":
            embed = discord.Embed(color=discord.utils.get(ctx.guild.roles, id=382557327892676619).color)
            embed.set_author(name="Libertarian Socialist", icon_url=z0diac.get_emoji(448477746138578944).url)
            embed.add_field(name="**Type:**", value="Umbrella Role")
            embed.add_field(name="**Wing:**", value="Left")
            embed.add_field(name="**Representative:**", value="Blade Holdin#3961")
            embed.add_field(name="**Members:**", value=str(len(discord.utils.get(ctx.guild.roles, id=382557327892676619).members)))
            embed.add_field(name="**Description:**", value="Libertarian Socialists/AnComs are distrusting of authority, opposing both the state and corporate power as a means to liberate people.")
            message = await ctx.channel.send(embed=embed)
        elif label == "SocDem" or label == "socdem" or label == "social democrat" or label == "Social Democrat" or label == "Social democrat" or label == "Socdem":
            embed = discord.Embed(color=discord.utils.get(ctx.guild.roles, id=381178125591117827).color)
            embed.set_author(name="Social Democrat", icon_url=z0diac.get_emoji(448477539233431563).url)
            embed.add_field(name="**Type:**", value="Umbrella Role")
            embed.add_field(name="**Wing:**", value="Left")
            embed.add_field(name="**Representative:**", value="Bear+Maiden=Faire#3513")
            embed.add_field(name="**Members:**", value=str(len(discord.utils.get(ctx.guild.roles, id=381178125591117827).members)))
            embed.add_field(name="**Description:**", value="Social Democrats believe in using government as a tool to bring about social progress and change. They lean authoritative, intersect with social justice, and are typically found on the left.")
            message = await ctx.channel.send(embed=embed)
        elif label == "green" or label == "Green" or label == "left libertarian":
            embed = discord.Embed(color=discord.utils.get(ctx.guild.roles, id=420735827023495169).color)
            embed.set_author(name="Green", icon_url=z0diac.get_emoji(448475108290592769).url)
            embed.add_field(name="**Type:**", value="Umbrella Role")
            embed.add_field(name="**Wing:**", value="Left")
            embed.add_field(name="**Representative:**", value="The Firebird#7278")
            embed.add_field(name="**Members:**", value=str(len(discord.utils.get(ctx.guild.roles, id=420735827023495169).members)))
            embed.add_field(name="**Description:**", value="Greens tend to be less about the economic liberty and more about the social and infrastructure liberty, especially on envrionmental issues. The open source community and net neutrality opponents are good examples of Greens.")
            message = await ctx.channel.send(embed=embed)
        elif label == "Neoliberal" or label == "neolib" or label == "neoliberal":
            embed = discord.Embed(color=discord.utils.get(ctx.guild.roles, id=381177002033676298).color)
            embed.set_author(name="Neoliberal", icon_url=z0diac.get_emoji(448479501018464256).url)
            embed.add_field(name="**Type:**", value="Umbrella Role")
            embed.add_field(name="**Wing:**", value="Center")
            embed.add_field(name="**Representative:**", value="Webhobo#4708")
            embed.add_field(name="**Members:**", value=str(len(discord.utils.get(ctx.guild.roles, id=381177002033676298).members)))
            embed.add_field(name="**Description:**", value="Neoliberalism mixes aspects of progressivism and classical liberalism to create an ideology that's moderate, pragmatic, and often focused on values such as globalism, lower government spending, and deregulation.")
            message = await ctx.channel.send(embed=embed)
        elif label == "centrist" or label == "Centrist":
            embed = discord.Embed(color=discord.utils.get(ctx.guild.roles, id=381176934131957760).color)
            embed.set_author(name="Centrist", icon_url=z0diac.get_emoji(448479331220455434).url)
            embed.add_field(name="**Type:**", value="Umbrella Role")
            embed.add_field(name="**Wing:**", value="Center")
            embed.add_field(name="**Representative:**", value="BowlOfPepper#2090")
            embed.add_field(name="**Members:**", value=str(len(discord.utils.get(ctx.guild.roles, id=381176934131957760).members)))
            embed.add_field(name="**Description:**", value="Centrists don't particularly lean any noticeable amount on the left/right scale; their policies are often moderate, and they focus on compromise over ideological passion. They can be anywhere on the authoritarian/libertarian scale.")
            message = await ctx.channel.send(embed=embed)
        elif label == "neocon" or label == "neoconservative" or label == "Neoconservative" or label == "Neocon":
            embed = discord.Embed(color=discord.utils.get(ctx.guild.roles, id=381176967631863810).color)
            embed.set_author(name="Neoconservative", icon_url=z0diac.get_emoji(448479686511689728).url)
            embed.add_field(name="**Type:**", value="Umbrella Role")
            embed.add_field(name="**Wing:**", value="Center")
            embed.add_field(name="**Representative:**", value="Kaiser Wilhelm II#3444")
            embed.add_field(name="**Members:**", value=str(len(discord.utils.get(ctx.guild.roles, id=381176967631863810).members)))
            embed.add_field(name="**Description:**", value="Neoconservatism is a foreign policy theory that builds on the idea that it's a democratic country's duty to spread its values through foreign intervention. On most issues but foreign policy, they tend to be more moderate.")
            message = await ctx.channel.send(embed=embed)
        elif label == "Paternalist" or label  == "paternalist":
            embed = discord.Embed(color=discord.utils.get(ctx.guild.roles, id=416369684179320834).color)
            embed.set_author(name="Paternalist", icon_url=z0diac.get_emoji(448478976252444673).url)
            embed.add_field(name="**Type:**", value="Umbrella Role")
            embed.add_field(name="**Wing:**", value="Right")
            embed.add_field(name="**Representative:**", value="PaxBritannicus#3672")
            embed.add_field(name="**Members:**", value=str(len(discord.utils.get(ctx.guild.roles, id=416369684179320834).members)))
            embed.add_field(name="**Description:**", value="Paternalists believe in the state taking a parent role, being authoritative on social policy, but interventionist economically.")
            message = await ctx.channel.send(embed=embed)
        elif label == "Theologue" or label == "theologue":
            embed = discord.Embed(color=discord.utils.get(ctx.guild.roles, id=409124661272641536).color)
            embed.set_author(name="Theologue", icon_url=z0diac.get_emoji(448479894725459968).url)
            embed.add_field(name="**Type:**", value="Umbrella Role")
            embed.add_field(name="**Wing:**", value="Center")
            embed.add_field(name="**Representative:**", value="JacolManuki#0703")
            embed.add_field(name="**Members:**", value=str(len(discord.utils.get(ctx.guild.roles, id=409124661272641536).members)))
            embed.add_field(name="**Description:**", value="Theologues are socially conservative, but vary widely on their economic policies. This includes Distributists, Christian Democrats, and right-theologues. Their main deciding factor in voting is their religion.")
            message = await ctx.channel.send(embed=embed)
        elif label == "Autocrat" or label == "autocrat":
            embed = discord.Embed(color=discord.utils.get(ctx.guild.roles, id=448633320431943682).color)
            embed.set_author(name="Autocrat", icon_url=z0diac.get_emoji(448636465417814026).url)
            embed.add_field(name="**Type:**", value="Umbrella Role")
            embed.add_field(name="**Wing:**", value="Center")
            embed.add_field(name="**Representative:**", value="Militaristic Cezar#6488")
            embed.add_field(name="**Members:**", value=str(len(discord.utils.get(ctx.guild.roles, id=448633320431943682).members)))
            embed.add_field(name="**Description:**", value="Third Positioners believe that the control of economic and social issues is best kept in the hands of a few or singular entities; they are economically incredibly authoritarian and interventionist, but differ on conservative/progressive.")
            message = await ctx.channel.send(embed=embed)
        elif label == "On Sale" or label == "for sale" or label == "For sale" or label == "forsale" or label == "Forsale" or label == "forSale":
            embed = discord.Embed(title="**Currently, we have the following items:**",description=" -ad\n -renamesaldol\n -memberplus\n -bigdab\n -subrole.\n -omegalounge\n Do `/whatis [Item]` to learn about pricing and descriptions.")
            embed.set_author(name="Effort Points Shop")
            message = await ctx.channel.send(embed=embed)
        elif label == "specs" or label == "Specs" or label == "yourspecs" or label== "your specs":
            await ctx.channel.send('**CPU:** Opteron 3365\n**GPU:** Radeon R7 360\n**HDD:** 320GB HDD\n**RAM:** 8GB DDR3\n**OS:** Kubuntu')
        elif label == "myBalance" or label == "mybalance" or label == "my balance":
            with open("dictionary.json", 'r') as f:
                repkey = json.load(f)
                await ctx.send(str(ctx.message.author.name) + " has " + str(repkey.get(str(ctx.message.author.id))) + ' Effort Points.')
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
                            message = await ctx.message.author.send("Your umbrella role is... **Autocrat**. Your subrole is... **Ethnonationalist**. If you have more questions or a more specific ideology to add, please DM Dakota.")
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
                                    message = await ctx.message.author.send("Your umbrella role is... **Autocrat**. Your subrole is... **Noocrat**. If you have more questions or a more specific ideology to add, please DM Dakota.")
                                if reaction36[0].emoji == '🇳':
                                    await message.remove_reaction('🇾', member=z0diac.user)
                                    message = await ctx.message.author.send("Your umbrella role is... **Autocrat**. Your subrole is... **Monarchist**. If you have more questions or a more specific ideology to add, please DM Dakota.")
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
                                message = await ctx.message.author.send("Your umbrella role is... **Autocrat**. Your subrole is... **Marxist-Leninist**. If you have more questions or a more specific ideology to add, please DM Dakota.")
                            if reaction41[0].emoji == '🇳':
                                await message.remove_reaction('🇾', member=z0diac.user)
                                message = await ctx.message.author.send("to add, p")
                        if reaction33[0].emoji == '🇳':
                            await message.remove_reaction('🇾', member=z0diac.user)
                            message = await ctx.message.author.send("Your umbrella role is... **Autocrat**. Your subrole is... **National Capitalist**. If you have more questions or a more specific ideology to add, please DM Dakota.")
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
        if 448475971553591300 == message:
            combinedset = (umbrella_roles & discord.utils.get(z0diac.get_all_members(), id=reacter).roles)
            await z0diac.get_guild(381170494814289922).get_member(reacter).remove_roles(combinedset)
            if str(reaction) == 448477016430215169:
                await z0diac.get_guild(381170494814289922).get_member(reacter).add_roles(discord.utils.get(z0diac.get_guild(381170494814289922).roles, id=443242847681118218))
                await discord.utils.get(z0diac.get_all_members(), id=reacter).send('You have been given the ' + discord.utils.get(z0diac.get_guild(381170494814289922), id=443242847681118218) + ' role.')
            elif str(reaction) == 448477539233431563:
                await z0diac.get_guild(381170494814289922).get_member(reacter).add_roles(discord.utils.get(z0diac.get_guild(381170494814289922).roles, id=381178125591117827))
                await z0diac.get_guild(381170494814289922).get_member(reacter).send('You have been given the ' + discord.utils.get(z0diac.get_guild(381170494814289922).roles, id=381178125591117827) + ' role.')
            elif str(reaction) == 448477746138578944:
                await z0diac.get_guild(381170494814289922).get_member(reacter).add_roles(discord.utils.get(z0diac.get_guild(381170494814289922).roles, id=382557327892676619))
                await z0diac.get_guild(381170494814289922).get_member(reacter).send('You have been given the ' + discord.utils.get(z0diac.get_guild(381170494814289922).roles, id=382557327892676619) + ' role.')
            elif str(reaction) == 448475108290592769:
                await z0diac.get_guild(381170494814289922).get_member(reacter).add_roles(discord.utils.get(z0diac.get_guild(381170494814289922).roles, id=420735827023495169))
                await z0diac.get_guild(381170494814289922).get_member(reacter).send('You have been given the ' + discord.utils.get(z0diac.get_guild(381170494814289922).roles, id=420735827023495169) + ' role.')
        elif 448476172343574528 == message:
            combinedset = (set(umbrella_roles) & set(discord.utils.get(z0diac.get_all_members(), id=reacter).roles)).pop()
            await z0diac.get_guild(381170494814289922).get_member(reacter).remove_roles(discord.utils.get(z0diac.get_guild(381170494814289922).roles, name=combinedset))
            if str(reaction) == 448479331220455434:
                combinedset = (set(umbrella_roles) & set(discord.utils.get(z0diac.get_all_members(), id=reacter).roles)).pop()
                await z0diac.get_guild(381170494814289922).get_member(reacter).remove_roles(discord.utils.get(z0diac.get_guild(381170494814289922).roles, name=combinedset))
                await z0diac.get_guild(381170494814289922).get_member(reacter).add_roles(discord.utils.get(z0diac.get_guild(381170494814289922).roles, id=381176934131957760))
                await discord.utils.get(z0diac.get_all_members(), id=reacter).send('You have been given the ' + discord.utils.get(z0diac.get_guild(381170494814289922).roles, id=381176934131957760) + ' role.')
            elif str(reaction) == 448479501018464256:
                await z0diac.get_guild(381170494814289922).get_member(reacter).add_roles(discord.utils.get(z0diac.get_guild(381170494814289922).roles, id=381177002033676298))
                await z0diac.get_guild(381170494814289922).get_member(reacter).send('You have been given the ' + discord.utils.get(z0diac.get_guild(381170494814289922).roles, id=381176934131957760) + ' role.')
            elif str(reaction) == 409124661272641536:
                await z0diac.get_guild(381170494814289922).get_member(reacter).add_roles(discord.utils.get(z0diac.get_guild(381170494814289922).roles, id=409124661272641536))
                await z0diac.get_guild(381170494814289922).get_member(reacter).send('You have been given the ' + discord.utils.get(z0diac.get_guild(381170494814289922).roles, id=409124661272641536) + ' role.')
            elif str(reaction) == 448479894725459968:
                await z0diac.get_guild(381170494814289922).get_member(reacter).add_roles(roles, id=381176967631863810)
                await z0diac.get_guild(381170494814289922).get_member(reacter).send('You have been given the ' + discord.utils.get(z0diac.get_guild(381170494814289922).roles, id=381176967631863810) + ' role.')
            elif str(reaction) == 448636465417814026:
                await z0diac.get_guild(381170494814289922).get_member(reacter).add_roles(discord.utils.get(z0diac.get_guild(381170494814289922).roles, id=448633320431943682))
                await z0diac.get_guild(381170494814289922).get_member(reacter).send('You have been given the ' + discord.utils.get(z0diac.get_guild(381170494814289922).roles, id=448633320431943682) + ' role.')
        elif 448476172343574528 == message:
            combinedset = (set(umbrella_roles) & set(discord.utils.get(z0diac.get_all_members(), id=reacter).roles)).pop()
            await z0diac.get_guild(381170494814289922).get_member(reacter).remove_roles(discord.utils.get(z0diac.get_guild(381170494814289922).roles, name=combinedset))
            if str(reaction) == 448478321743888406:
                await z0diac.get_guild(381170494814289922).get_member(reacter).add_roles(discord.utils.get(z0diac.get_guild(381170494814289922).roles, id=427819576882102273))
                await discord.utils.get(z0diac.get_all_members(), id=reacter).send('You have been given the ' + discord.utils.get(z0diac.get_guild(381170494814289922).roles, id=427819576882102273) + ' role.')
            elif str(reaction) == 448478811076427786:
                await z0diac.get_guild(381170494814289922).get_member(reacter).add_roles(discord.utils.get(z0diac.get_guild(381170494814289922).roles, id=381177029464293386))
                await z0diac.get_guild(381170494814289922).get_member(reacter).send('You have been given the ' + discord.utils.get(z0diac.get_guild(381170494814289922).roles, id=381177029464293386) + ' role.')
            elif str(reaction) == 448478542444101643:
                await z0diac.get_guild(381170494814289922).get_member(reacter).add_roles(discord.utils.get(z0diac.get_guild(381170494814289922).roles, id=381177107616759810))
                await z0diac.get_guild(381170494814289922).get_member(reacter).send('You have been given the ' + discord.utils.get(z0diac.get_guild(381170494814289922).roles, id=381177107616759810) + ' role.')
            elif str(reaction) == 448478976252444673:
                await z0diac.get_guild(381170494814289922).get_member(reacter).add_roles(discord.utils.get(z0diac.get_guild(381170494814289922).roles, id=416369684179320834))
                await z0diac.get_guild(381170494814289922).get_member(reacter).send('You have been given the ' + discord.utils.get(z0diac.get_guild(381170494814289922).roles, id=416369684179320834) + ' role.')
            elif str(reaction) == 448478976252444673:
                await z0diac.get_guild(381170494814289922).get_member(reacter).add_roles(discord.utils.get(z0diac.get_guild(381170494814289922).roles, id=424645022927945736))
                await z0diac.get_guild(381170494814289922).get_member(reacter).send('You have been given the ' + discord.utils.get(z0diac.get_guild(381170494814289922), id=424645022927945736) + ' role.')
        elif 448486263608049666 == message:
            await z0diac.get_guild(381170494814289922).get_member(reacter).add_roles(discord.utils.get(z0diac.get_guild(381170494814289922).roles,id=409483695582478348))
            await z0diac.get_guild(381170494814289922).get_member(reacter).send('You have been given the Apolitical role.')
        elif str(reaction) == '📌' or str(reaction) == '📍':
            with open("dictionary.json", 'r+') as f:
                    if z0diac.get_channel(446400765775314947):
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
        if ctx.channel != z0diac.get_channel(432574353822056448):
            if ctx.message.content[5:] == 'bigdab' or ctx.message.content[:5] == 'dab':
                    dollar_amount = 2
                    if currentvalue_customer - dollar_amount >= 0:
                        repkey[str(ctx.message.author.id)] = currentvalue_customer - dollar_amount
                        f.seek(0)
                        json.dump(repkey, f)
                        f.truncate()
                        with open('bigdab.png','rb') as image:
                            await ctx.channel.send(file=image)
                    else:
                        await ctx.channel.send('You need 2 EP to do that!')
            elif ctx.message.content[5:17] == 'renamesaldol':
                if ctx.message.author != discord.utils.get(ctx.guild.members, id=173451290268008448):
                    saldol = ctx.guild.get_member(173451290268008448)
                    saldolname = saldol.display_name
                    currentvalue_saldol = repkey.get(str(173451290268008448))
                    dollar_amount = 5
                    if currentvalue_customer - dollar_amount >= 0:
                            repkey[str(ctx.message.author.id)] = currentvalue_customer - dollar_amount
                            f.seek(0)
                            json.dump(repkey, f)
                            f.truncate()
                    try:
                        await saldol.edit(nick=ctx.message.content[18:])
                        await ctx.channel.trigger_typing()
                        time.sleep(3)
                        aftersaldol = saldol.display_name
                        await ctx.channel.send(saldolname + ', more like ' + aftersaldol + '!')
                        repkey[str(173451290268008448)] = currentvalue_saldol + 2
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
                embed = discord.Embed(title=(ctx.message.author.display_name + " (" + ctx.message.created_at.strftime("%Y-%m-%d %H:%M:%S") + ")"), color=ctx.message.author.color, description=ctx.message.content[12:])
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


@z0diac.command()
async def optinlounge(ctx):
    await ctx.message.author.add_roles(discord.utils.get(ctx.guild.roles,id=447429561366478849))

z0diac.run("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
