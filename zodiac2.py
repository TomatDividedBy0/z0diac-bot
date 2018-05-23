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
        elif label == "Autocrat" or label == "autocrat":
            await ctx.channel.send("Third Positioners believe that the control of economic and social issues is best kept in the hands of a few or singular entities; they are economically incredibly authoritarian and interventionist, but differ on conservative/progressive.")
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
                                        message = await ctx.message.author.send("Question 9: Do you believe society has to be fundamentally changed in order to progress?")
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
                                message = await ctx.message.author.send("Question 9: Do you believe society has to be fundamentally changed in order to progress?")
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
                        message = await ctx.message.author.send("**Question 4:**\nShould the government serve the working class over the private sector?")
                        await message.add_reaction('🇾')
                        await message.add_reaction('🇳')
                        def check(reaction, user):
                            return reaction.count == 2
                        reaction33 = await z0diac.wait_for('reaction_add', check=check)
                        if reaction33[0].emoji == '🇾':
                            await message.remove_reaction('🇳', member=z0diac.user)
                            message = await ctx.message.author.send("Your umbrella role is... **Autocrat**. Your subrole is... **Marxist-Leninist**. If you have more questions or a more specific ideology to add, please DM Dakota.")
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
            await ctx.channel.send("bigdab is a shop item that allows you to post a full-sized dab instead of a tiny emote. This item costs you 10 EP.")
        elif label == "renamefuco" or label == "renameFuCo" or label == "rename FuCo":
            await ctx.channel.send("renamefuco is a shop item that allows you to rename FuCo, AKA BottomKek13 to whatever you desire; yes, he is not allowed to change whatever you give him. This item costs you 25 EP.")
        elif label == "membership" or label == "Membership" or label == "loungekey":
            await ctx.channel.send("The membership, AKA the Lounge Key, is a shop item that gives you the Member+ role and the ability to visit the off topic lounge. This item costs you 300 EP.")
        elif label == "ad" or label == "Ad" or label == "advertisement":
            await ctx.channel.send("ad is a shop item that allows you to advertise one message on the billboard channel for everyone to see. This item costs you 75 EP.")
        elif label == "subrole" or label == "Subrole" or label == "sub role":
            await ctx.channel.send("subrole is a shop item that gives you a role to tag yourself with. This item costs you 125 EP.")
        elif label == "suggest":
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
    if reacter != z0diac.user.id:
        roles = z0diac.get_channel(channel).guild.roles
        umbrella_roles = [discord.utils.get(roles, id=420735827023495169), discord.utils.get(roles, id=443242847681118218), discord.utils.get(roles, id=381178125591117827),discord.utils.get(roles, id=382557327892676619), discord.utils.get(roles, id=420735827023495169), discord.utils.get(roles, id=381176934131957760), discord.utils.get(roles, id=381177002033676298), discord.utils.get(roles, id=409124661272641536), discord.utils.get(roles, id=381176967631863810), discord.utils.get(roles, id=448633320431943682), discord.utils.get(roles, id=381177029464293386), discord.utils.get(roles, id=427819576882102273), discord.utils.get(roles, id=381177107616759810), discord.utils.get(roles, id=416369684179320834), discord.utils.get(roles, id=424645022927945736), discord.utils.get(roles, id=409483695582478348)]
        print(umbrella_roles)
        print(discord.utils.get(z0diac.get_all_members(), id=reacter).roles)
        if 448475971553591300 == message:
            if str(reaction) == 448477016430215169:
                for x in discord.utils.get(z0diac.get_all_members(), id=reacter).roles:
                    for y in umbrella_roles:
                        await discord.utils.get(z0diac.get_all_members(), id=reacter).remove_roles(x)
                await z0diac.get_guild(381170494814289922).get_member(reacter).add_roles(discord.utils.get(z0diac.get_guild(381170494814289922).guild.roles, id=443242847681118218))
                await discord.utils.get(z0diac.get_all_members(), id=reacter).send('You have been given the ' + discord.utils.get(z0diac.get_guild(381170494814289922), id=443242847681118218) + ' role.')
            elif str(reaction) == 448477539233431563:
                for x in discord.utils.get(z0diac.get_all_members(), id=reacter).roles:
                    if x in umbrella_roles:
                        await discord.utils.get(z0diac.get_all_members(), id=reacter).remove_roles(x)
                await z0diac.get_guild(381170494814289922).get_member(reacter).add_roles(discord.utils.get(z0diac.get_guild(381170494814289922).guild.roles, id=381178125591117827))
                await z0diac.get_guild(381170494814289922).get_member(reacter).send('You have been given the ' + discord.utils.get(z0diac.get_guild(381170494814289922).roles, id=381178125591117827) + ' role.')
            elif str(reaction) == 448477746138578944:
                for x in discord.utils.get(z0diac.get_all_members(), id=reacter).roles:
                    if x in umbrella_roles:
                        await discord.utils.get(z0diac.get_all_members(), id=reacter).remove_roles(x)
                await z0diac.get_guild(381170494814289922).get_member(reacter).add_roles(discord.utils.get(z0diac.get_guild(381170494814289922).guild.roles, id=382557327892676619))
                await z0diac.get_guild(381170494814289922).get_member(reacter).send('You have been given the ' + discord.utils.get(z0diac.get_guild(381170494814289922).roles, id=382557327892676619) + ' role.')
            elif str(reaction) == 448475108290592769:
                for x in discord.utils.get(z0diac.get_all_members(), id=reacter).roles:
                    if x in umbrella_roles:
                        await discord.utils.get(z0diac.get_all_members(), id=reacter).remove_roles(x)
                await z0diac.get_guild(381170494814289922).get_member(reacter).add_roles(discord.utils.get(z0diac.get_guild(381170494814289922).roles, id=420735827023495169))
                await z0diac.get_guild(381170494814289922).get_member(reacter).send('You have been given the ' + discord.utils.get(z0diac.get_guild(381170494814289922).roles, id=420735827023495169) + ' role.')
        elif 448476172343574528 == message:
            if str(reaction) == 448479331220455434:
                for x in discord.utils.get(z0diac.get_all_members(), id=reacter).roles:
                    if x in umbrella_roles:
                        await discord.utils.get(z0diac.get_all_members(), id=reacter).remove_roles(x)
                await z0diac.get_guild(381170494814289922).get_member(reacter).add_roles(discord.utils.get(z0diac.get_guild(381170494814289922).guild.roles, id=381176934131957760))
                await discord.utils.get(z0diac.get_all_members(), id=reacter).send('You have been given the ' + discord.utils.get(z0diac.get_guild(381170494814289922).roles, id=381176934131957760) + ' role.')
            elif str(reaction) == 448479501018464256:
                for x in discord.utils.get(z0diac.get_all_members(), id=reacter).roles:
                    if x in umbrella_roles:
                        await discord.utils.get(z0diac.get_all_members(), id=reacter).remove_roles(x)
                await z0diac.get_guild(381170494814289922).get_member(reacter).add_roles(discord.utils.get(z0diac.get_guild(381170494814289922).guild.roles, id=381177002033676298))
                await z0diac.get_guild(381170494814289922).get_member(reacter).send('You have been given the ' + discord.utils.get(z0diac.get_guild(381170494814289922).roles, id=381176934131957760) + ' role.')
            elif str(reaction) == 409124661272641536:
                for x in discord.utils.get(z0diac.get_all_members(), id=reacter).roles:
                    if x in umbrella_roles:
                        await discord.utils.get(z0diac.get_all_members(), id=reacter).remove_roles(x)
                await z0diac.get_guild(381170494814289922).get_member(reacter).add_roles(discord.utils.get(z0diac.get_guild(381170494814289922).guild.roles, id=409124661272641536))
                await z0diac.get_guild(381170494814289922).get_member(reacter).send('You have been given the ' + discord.utils.get(z0diac.get_guild(381170494814289922).roles, id=409124661272641536) + ' role.')
            elif str(reaction) == 448479894725459968:
                for x in discord.utils.get(z0diac.get_all_members(), id=reacter).roles:
                    if x in umbrella_roles:
                        await discord.utils.get(z0diac.get_all_members(), id=reacter).remove_roles(x)
                await z0diac.get_guild(381170494814289922).get_member(reacter).add_roles(discord.utils.get(z0diac.get_guild(381170494814289922).roles, id=381176967631863810))
                await z0diac.get_guild(381170494814289922).get_member(reacter).send('You have been given the ' + discord.utils.get(z0diac.get_guild(381170494814289922).roles, id=381176967631863810) + ' role.')
            elif str(reaction) == 448636465417814026:
                for x in discord.utils.get(z0diac.get_all_members(), id=reacter).roles:
                    if x in umbrella_roles:
                        await discord.utils.get(z0diac.get_all_members(), id=reacter).remove_roles(x)
                await z0diac.get_guild(381170494814289922).get_member(reacter).add_roles(discord.utils.get(z0diac.get_guild(381170494814289922).guild.roles, id=448633320431943682))
                await z0diac.get_guild(381170494814289922).get_member(reacter).send('You have been given the ' + discord.utils.get(z0diac.get_guild(381170494814289922).guild.roles, id=448633320431943682) + ' role.')
        elif 448476172343574528 == message:
            if str(reaction) == 448478321743888406:
                for x in discord.utils.get(z0diac.get_all_members(), id=reacter).roles:
                    if x in umbrella_roles:
                        await discord.utils.get(z0diac.get_all_members(), id=reacter).remove_roles(x)
                await z0diac.get_guild(381170494814289922).get_member(reacter).add_roles(discord.utils.get(z0diac.get_guild(381170494814289922).guild.roles, id=427819576882102273))
                await discord.utils.get(z0diac.get_all_members(), id=reacter).send('You have been given the ' + discord.utils.get(z0diac.get_guild(381170494814289922).roles, id=427819576882102273) + ' role.')
            elif str(reaction) == 448478811076427786:
                for x in discord.utils.get(z0diac.get_all_members(), id=reacter).roles:
                    if x in umbrella_roles:
                        await discord.utils.get(z0diac.get_all_members(), id=reacter).remove_roles(x)
                await z0diac.get_guild(381170494814289922).get_member(reacter).add_roles(discord.utils.get(z0diac.get_guild(381170494814289922).roles, id=381177029464293386))
                await z0diac.get_guild(381170494814289922).get_member(reacter).send('You have been given the ' + discord.utils.get(z0diac.get_guild(381170494814289922).roles, id=381177029464293386) + ' role.')
            elif str(reaction) == 448478542444101643:
                for x in discord.utils.get(z0diac.get_all_members(), id=reacter).roles:
                    if x in umbrella_roles:
                        await discord.utils.get(z0diac.get_all_members(), id=reacter).remove_roles(x)
                await z0diac.get_guild(381170494814289922).get_member(reacter).add_roles(discord.utils.get(z0diac.get_guild(381170494814289922).roles, id=381177107616759810))
                await z0diac.get_guild(381170494814289922).get_member(reacter).send('You have been given the ' + discord.utils.get(z0diac.get_guild(381170494814289922).roles, id=381177107616759810) + ' role.')
            elif str(reaction) == 448478976252444673:
                for x in discord.utils.get(z0diac.get_all_members(), id=reacter).roles:
                    if x in umbrella_roles:
                        await discord.utils.get(z0diac.get_all_members(), id=reacter).remove_roles(x)
                await z0diac.get_guild(381170494814289922).get_member(reacter).add_roles(discord.utils.get(z0diac.get_guild(381170494814289922).roles, id=416369684179320834))
                await z0diac.get_guild(381170494814289922).get_member(reacter).send('You have been given the ' + discord.utils.get(z0diac.get_guild(381170494814289922).roles, id=416369684179320834) + ' role.')
            elif str(reaction) == 448478976252444673:
                for x in discord.utils.get(z0diac.get_all_members(), id=reacter).roles:
                    if x in umbrella_roles:
                        await discord.utils.get(z0diac.get_all_members(), id=reacter).remove_roles(x)
                await z0diac.get_guild(381170494814289922).get_member(reacter).add_roles(discord.utils.get(z0diac.get_guild(381170494814289922).guild.roles, id=424645022927945736))
                await z0diac.get_guild(381170494814289922).get_member(reacter).send('You have been given the ' + discord.utils.get(z0diac.get_guild(381170494814289922), id=424645022927945736) + ' role.')
        elif 448486263608049666 == message:
            await z0diac.get_guild(381170494814289922).get_member(reacter).add_roles(discord.utils.get(z0diac.get_guild(381170494814289922).roles,id=409483695582478348))
            await z0diac.get_guild(381170494814289922).get_member(reacter).send('You have been given the Apolitical role.')
        elif str(reaction) == '📌' or str(reaction) == '📍':
            if z0diac.get_channel(446400765775314947):
                x = await discord.utils.get(z0diac.get_all_channels(), id=channel).get_message(message)
                embed = discord.Embed(title=(x.author.display_name + " (" + x.created_at.strftime("%Y-%m-%d %H:%M:%S") + ")"), color=x.author.color, description=x.content)
                embed.set_thumbnail(url=x.author.avatar_url)
                msg = await z0diac.get_channel(446400765775314947).send(embed=embed)
                for x in z0diac.get_channel(446400765775314947).history:
                    if msg.content == x:
                        msg.channel.delete_messages(msg)



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
            elif ctx.message.content[5:10] == 'topic':
                if discord.utils.get(ctx.guild.roles, id=448902429275324427) in ctx.message.author.roles:
                    dollar_amount = 0
                else:
                    dollar_amount = 30
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
async def suggest(ctx):
    embed = discord.Embed(title=(ctx.message.author.display_name + " (" + ctx.message.created_at.strftime("%Y-%m-%d %H:%M:%S") + ")"), color=ctx.message.author.color, description=ctx.message.content[9:])
    embed.set_thumbnail(url=ctx.message.author.avatar_url)
    message = await z0diac.get_channel(448905798509264906).send(embed=embed)
    await message.add_reaction('✅')
    await message.add_reaction('❎')
    await ctx.message.delete()

z0diac.run("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
