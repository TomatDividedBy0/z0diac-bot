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
    print(ctx.message.content[8:])
    if ctx.message.content[8:] == "Socialist" or ctx.message.content[8:] == "socialist" or ctx.message.content[8:] == "Socialists" or ctx.message.content[8:] == "socialists":
        await ctx.channel.send("Socialists believe in the public ownership of the means of production. They are commonly found on the far-left end of the compass, with varying degrees of authoritarianism/libertarianism.")
    elif ctx.message.content[8:] == "Classical Liberal" or ctx.message.content[8:] == "classical liberal" or ctx.message.content[8:] == "classical lib" or ctx.message.content[8:] == "Classical liberal" or ctx.message.content[8:] == "Classical Lib" or ctx.message.content[8:] == "Classical lib":
        await ctx.message.channel.send("Classical liberals adhere strongly to the rights of the individual, however, unlike libertarians, they are a lot more moderate on the free market. You'll usually find them straight down from center or near center.")
    elif ctx.message.content[8:] == "Nationalist" or ctx.message.content[8:] == "nationalist":
        await ctx.message.channel.send("Nationalists believe in putting their own country or group first above others. They are often protectionist, and come in many different variants from Civic Nationalists to NazBols to Ethnonationalists.")
    elif ctx.message.content[8:] == "Right Libertarian" or ctx.message.content[8:] == "Libertarian" or ctx.message.content[8:] == "libertarian" or ctx.message.content[8:] == "right libertarian":
        await ctx.message.channel.send("Libertarians tend to favor solutions that involve the free market and the individual over government intervention, detesting excess public spending and tax hikes. They are found everywhere on the bottom right of the compass.")
    elif ctx.message.content[8:] == "Paleoconservative" or ctx.message.content[8:] == "paleocon" or ctx.message.content[8:] == "paleoconservative" or ctx.message.content[8:] == "paleocon":
        await ctx.channel.send("Paleoconservatives, also known as the Old Right, date back to the early 20th century in their beliefs. They place social tradition and economic nonintervention above all else, often being in the top right of the compass.")
    elif ctx.message.content[8:] == "LibtSoc" or ctx.message.content[8:] == "Libertarian Socialist" or ctx.message.content[8:] == "Libertarian Socialist" or ctx.message.content[8:] == "libertarian socialist":
        await ctx.channel.send(" Libertarian Socialists/AnComs advocate for the abolition of state and private property as a means to liberate people.")
    elif ctx.message.content[8:] == "SocDem" or ctx.message.content[8:] == "socdem" or ctx.message.content[8:] == "social democrat" or ctx.message.content[8:] == "Social Democrat" or ctx.message.content[8:] == "Social democrat" or ctx.message.content[8:] == "Socdem":
        await ctx.channel.send("Social Democrats believe in using government as a tool to bring about social progress and change. They lean authoritative, intersect with social justice, and are typically found on the left.")
    elif ctx.message.content[8:] == "green" or ctx.message.content[8:] == "Green" or ctx.message.content[8:] == "left libertarian":
        await ctx.channel.send("Greens tend to be less about the economic liberty and more about the social and infrastructure liberty, especially on envrionmental issues. The open source community and net neutrality opponents are good examples of Greens.")
    elif ctx.message.content[8:] == "Neoliberal" or ctx.message.content[8:] == "neolib" or ctx.message.content[8:] == "neoliberal":
        await ctx.channel.send("Neoliberalism mixes aspects of progressivism and classical liberalism to create an ideology that's moderate, pragmatic, and often focused on values such as globalism, lower government spending, and deregulation.")
    elif ctx.message.content[8:] == "centrist" or ctx.message.content[8:] == "Centrist":
        await ctx.channel.send("Centrists don't particularly lean any noticeable amount on the left/right scale; their policies are often moderate, and they focus on compromise over ideological passion. They can be anywhere on the authoritarian/libertarian scale.")
    elif ctx.message.content[8:] == "neocon" or ctx.message.content[8:] == "neoconservative" or ctx.message.content[8:] == "Neoconservative" or ctx.message.content[8:] == "Neocon":
        await ctx.channel.send("Neoconservatism is a foreign policy theory that builds on the idea that it's a democratic country's duty to spread its values through foreign intervention. On most issues but foreign policy, they tend to be more moderate.")
    elif ctx.message.content[8:] == "Paternalist" or ctx.message.content[8:]  == "paternalist":
        await ctx.channel.send("Paternalists believe in the state taking a parent role, being authoritative on social policy, but interventionist economically.")
    elif ctx.message.content[8:] == "Paleoliberal" or ctx.message.content[8:] == "Paleolib" or ctx.message.content[8:] == "paleoliberal" or ctx.message.content[8:] == "paleolib":
        await ctx.channel.send("A paleoliberal or a RINO/Whig in the US is a term for a conservative who is a lot more moderate and centrist in their beliefs. They typically are found close to the center on issues of tradition, being economically to the right, typically being the parallel to Blue Dogs.")
    elif ctx.message.content[8:] == "Theologue" or ctx.message.content[8:] == "theologue":
        await ctx.channel.send("Theologues are socially conservative, but vary widely on their economic policies. This includes Distributists, Christian Democrats, and right-theologues. Their main deciding factor in voting is their religion.")
    else:
        await ctx.channel.send(ctx.message.content[8:] + " is not a role.")


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
z0diac.run("MzgzMzg1MTk4NTM0MDY2MTg3.DdOKNg.k92hJ_rHCjllSa_ehn81b2s9uNk")

