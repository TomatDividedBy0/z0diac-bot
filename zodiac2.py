import discord
from discord.ext import commands

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
    print(label)
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
    else:
        await ctx.channel.send(label + " is not a role.")

        
@z0diac.command()
async def define(ctx):
    word = ctx.message.content[7:]
    meaningobject = dictionary.meaning(word)
    definition = next(iter(meaningobject.values()))[0]
    await ctx.channel.send(ctx.message.content[7:] + "means " + definition)
@z0diac.command()
async def rolequiz(ctx):
    await ctx.message.author.send("Welcome to the official compact edition of the PWH political test. \nYou will be asked various questions on your values to determine your ideology. Simply say ready when you are ready to start.")
    def check(message):
        return message.author == ctx.message.author and message.channel == discord.DMChannel and message.content == 'ready'
    message = await z0diac.wait_for('message', check=check)
    print(str(message.author.id) + ': This is message.author')
    print(str(message.channel.id) + ': This is message.channel')
    print(str(message.author.id) + ': This is message.content')
    print(str(ctx.message.author.id) + ': This is ctx.message.author')
    print(str(discord.DMChannel.id) + ': This is message.author')
    if message.author == ctx.message.author and message.channel == discord.DMChannel and message.content == 'ready':
        await ctx.message.author.send("Welcome to the official compact edition of the PWH political test. \nYou will be asked various questions on your values to determine your ideology. Simply send a thumbs up emoji to begin.")
    else:
        print("Fail")
z0diac.run("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")

