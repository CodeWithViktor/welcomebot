# Import necessary packages 
import discord
import os
import json
from discord.ext import commands

# Setting Intents
intents = discord.Intents.default()
intents.members = True  # Subscribe to member events
intents.presences = True  # Subscribe to presence events
intents.message_content = True
bot = commands.Bot(command_prefix='+', intents=intents)

# Events and Status
@bot.event
async def on_ready():
    await bot.tree.sync()
    print(f'{bot.user} has connected to Discord!')
    await bot.change_presence(status=discord.Status.online, activity=discord.Game('+help | CodeWithViktor'))

# Commands
# 1) Help Command
bot.remove_command('help')
@bot.command(name='help')
async def help(ctx):
    embed = discord.Embed(title="Help", color=0x00ff00)
    embed.add_field(name="**__General Commands__**", value="`+about`: Gives information about this bot!\n`+aboutdev`: Gives information about bot's developer!\n`+ping`: Checks the bot's latency!", inline=False)
    embed.add_field(name="**__Moderation Commands__**", value="`+setwelcome`: Setup for embed welcome message!\n`+deletewelcome`: Removes the setup for the welcome message!", inline=False)
    embed.set_footer(text='Made by @CodeWithViktor')
    await ctx.send(embed=embed)

# 2) About command
@bot.command(name='about')
async def about(ctx):
    embed = discord.Embed(title="Bot Information", color=0x00ff00)
    embed.description = f"**<@1263731650593030144> is here to enhance your experience and ensure you feel right at home from the moment you join. Here’s what <@1263731650593030144> does:**\n\n"
    embed.add_field(name="**Greeting New Members:**", value="As soon as you join the server, our Welcome Bot sends you a warm welcome message. This helps in creating a friendly atmosphere and makes you feel valued right away.", inline=False)
    embed.add_field(name="**Introduction to the Community:**", value="The Bot provides essential information about our community, such as rules, guidelines, and how to get started. This ensures that everyone understands our expectations and can dive into discussions smoothly.", inline=False)
    embed.add_field(name="**Customizable Messages:**", value="We understand that personalization matters. Our Welcome Bot allows us to customize messages, so each new member feels acknowledged and appreciated in their unique way.", inline=False)
    embed.add_field(name="**Invite the bot:**", value="[Click Here to invite the bot](https://discord.com/oauth2/authorize?client_id=1263731650593030144&permissions=1206080613616&response_type=code&redirect_uri=https%3A%2F%2Fdiscord.com%2Foauth2%2Fauthorize%3Fclient_id%3D1263731650593030144&integration_type=0&scope=bot+identify)", inline=False)
    embed.set_footer(text='Made by @CodeWithViktor')
    await ctx.send(embed=embed)

# 3) Dev Info Command [Don't remove mycredit, else do as you want]
@bot.command(name='aboutdev')
async def aboutdev(ctx):
    embed = discord.Embed(title="About Developer", color=0x00ff00)
    embed.description = f"The creator of bot is Dr. Viktor"
    embed.set_footer(text='Made by @CodeWithViktor')
    await ctx.send(embed=embed)

# 4) Ping Command
@bot.command(name='ping')
async def ping(ctx):
    latency = bot.latency * 1000
    embed = discord.Embed(description=f'Pong! My latency is {latency:.2f}ms', color=0x00ff00)
    embed.set_footer(text='Made by @CodeWithViktor')
    await ctx.send(embed=embed)

# 5) welcomemessage command (Don't try to change anything)
@bot.command(name='setwelcome')
@commands.has_permissions(manage_guild=True)
async def setwelcome(ctx):
    if os.path.exists('setwelcome.json'):
        with open('setwelcome.json', 'r') as f:
            setwelcome_data = json.load(f)

        if str(ctx.guild.id) in setwelcome_data:
            embed = discord.Embed(title='**Welcome Embed Message Setup**', color=0x00ff00)
            embed.add_field(name='Setup already exists!', value='Do you want to reset the setup? (yes/no)', inline=False)
            await ctx.send(embed=embed)

            def check(message):
                return message.author == ctx.author and message.channel == ctx.channel

            msg = await bot.wait_for('message', check=check)
            if msg.content.lower() == 'yes':
                setwelcome_data.pop(str(ctx.guild.id), None)
                with open('setwelcome.json', 'w') as f:
                    json.dump(setwelcome_data, f)
                await ctx.send('Setup reset! Please set up the welcome embed message again.')
                return
            else:
                await ctx.send('Setup not reset. You can use the `+welcomemessage` command again to reset the setup.')
                return

    if os.path.exists('setwelcome.json'):
        with open('setwelcome.json', 'r') as f:
            setwelcome_data = json.load(f)
    else:
        setwelcome_data = {}

    embed = discord.Embed(title='**Welcome Embed Message Setup**', color=0x00ff00)
    embed.add_field(name='Channel', value='Please enter the channel ID or mention the channel where you want to send the welcome embed message.', inline=False)
    await ctx.send(embed=embed)

    def check(message):
        return message.author == ctx.author and message.channel == ctx.channel

    msg = await bot.wait_for('message', check=check)

    if msg.channel_mentions:
        channel = msg.channel_mentions[0]
    else:
        try:
            channel_id = int(msg.content)
            channel = bot.get_channel(channel_id)
        except ValueError:
            embed = discord.Embed(title='**Welcome Embed Message Setup**', color=0xff0000)
            embed.add_field(name='Error!', value='Invalid channel ID or mention. Please try again.', inline=False)
            await ctx.send(embed=embed)
            return

    embed = discord.Embed(title='**Welcome Embed Message Setup**', color=0x00ff00)
    embed.add_field(name='Header', value='Please enter the header for the welcome embed message.', inline=False)
    await ctx.send(embed=embed)

    msg = await bot.wait_for('message', check=check)
    header = msg.content

    embed = discord.Embed(title='**Welcome Embed Message Setup**', color=0x00ff00)
    embed.add_field(name='Description', value='Please enter the description for the welcome embed message.', inline=False)
    await ctx.send(embed=embed)

    msg = await bot.wait_for('message', check=check)
    description = msg.content

    embed = discord.Embed(title='**Welcome Embed Message Setup**', color=0x00ff00)
    embed.add_field(name='Footer', value='Please enter the footer for the welcome embed message.', inline=False)
    await ctx.send(embed=embed)

    msg = await bot.wait_for('message', check=check)
    footer = msg.content

    embed = discord.Embed(title='**Welcome Embed Message Setup**', color=0x00ff00)
    embed.add_field(name='Color', value='Please enter the color for the welcome embed message (in hex format, e.g. #ffffff).', inline=False)
    await ctx.send(embed=embed)

    msg = await bot.wait_for('message', check=check)
    color = int(msg.content.lstrip('#'), 16)

    setwelcome_data[str(ctx.guild.id)] = {
        'channel_id': channel.id,
        'header': header,
        'description': description,
        'footer': footer,
        'color': color
    }

    with open('setwelcome.json', 'w') as f:
        json.dump(setwelcome_data, f)

    embed = discord.Embed(title='**Welcome Embed Message Setup**', color=0x00ff00)
    embed.add_field(name='Success!', value='Welcome embed message setup complete!', inline=False)
    await ctx.send(embed=embed)

@bot.event
async def on_member_join(member):
    with open('setwelcome.json', 'r') as f:
        setwelcome_data = json.load(f)

    if str(member.guild.id) in setwelcome_data:
        channel_id = setwelcome_data[str(member.guild.id)]['channel_id']
        channel = bot.get_channel(channel_id)
        header = setwelcome_data[str(member.guild.id)]['header']
        description = setwelcome_data[str(member.guild.id)]['description']
        footer = setwelcome_data[str(member.guild.id)]['footer']
        color = setwelcome_data[str(member.guild.id)]['color']

        embed = discord.Embed(title=header, description=description, color=color)
        embed.set_footer(text=footer)

        await channel.send(f'Welcome {member.mention} to the server!', embed=embed)

# 6) deletewcmessage
@bot.command(name='deletewelcome')
@commands.has_permissions(manage_guild=True)
async def deletewelcome(ctx):
    if os.path.exists('setwelcome.json'):
        with open('setwelcome.json', 'r') as f:
            setwelcome_data = json.load(f)

        if str(ctx.guild.id) in setwelcome_data:
            setwelcome_data.pop(str(ctx.guild.id), None)
            with open('setwelcome.json', 'w') as f:
                json.dump(setwelcome_data, f)

            embed = discord.Embed(title='**Welcome Embed Message Setup**', color=0x00ff00)
            embed.add_field(name='Success!', value='Welcome embed message setup deleted!', inline=False)
            await ctx.send(embed=embed)
        else:
            embed = discord.Embed(title='**Welcome Embed Message Setup**', color=0xff0000)
            embed.add_field(name='Error!', value='No welcome embed message setup found for this server.', inline=False)
            await ctx.send(embed=embed)
    else:
        embed = discord.Embed(title='**Welcome Embed Message Setup**', color=0xff0000)
        embed.add_field(name='Error!', value='No welcome embed message setup found for this server.', inline=False)
        await ctx.send(embed=embed)

# BOT_TOKEN
bot.run('')