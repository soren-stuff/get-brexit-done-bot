from http import client
import discord
from discord.ext import commands
from requests import get
import random

bot = discord.Bot()

@bot.event
async def on_ready():
    print("just save me".format(bot))

    # Stats

@bot.slash_command(guild_ids=[871168657382838292, 827650989070090340, 908816464784552026, 964167989916213318, 880890047962955809])
async def stats(ctx, self):
    """This displays the election results"""
    count = str(len(bot.guilds))
    stats_embed = discord.Embed(
        description=f"This is where we show our quaterly income from scamming 60 year olds into voting for Boris (See: Granny Farming)",
        colour=0xfff673
        )
    stats_embed.add_field(name="creator", value="soren#8898", inline=True)
    stats_embed.add_field(name="commands", value="at *least* 7", inline=True)
    stats_embed.add_field(name="servers in", value=str(count))
    stats_embed.set_footer(text="This is v1.0! Find the code at https://github.com/soren-stuff/get-brexit-done-bot", icon_url="https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/160/twitter/53/flushed-face_1f633.png")
    await ctx.respond(embed=stats_embed)

@bot.slash_command(guild_ids=[871168657382838292, 827650989070090340, 908816464784552026, 964167989916213318, 880890047962955809])
async def about(ctx):
    """Tells you about the bot"""
    about_embed = discord.Embed(
        description=f"We needed to get brexit done.\nWith this bot, we can do so.",
        title="GBD Bot"
    )
    about_embed.set_footer(text="Support server: https://discord.gg/tKGCnmBUvH", icon_url="https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/160/twitter/53/flushed-face_1f633.png")
    about_embed.set_image(url="https://media.discordapp.net/attachments/789850729124462592/967406768592400384/unknown.png?width=896&height=910")
    await ctx.respond(embed=about_embed)




# Moderation Commands



@bot.slash_command(guild_ids=[871168657382838292, 827650989070090340, 908816464784552026, 964167989916213318, 880890047962955809])
@commands.has_permissions(ban_members = True)
async def outcasting(ctx, libdem : discord.Member, reason : str):
    """Have someone leave the Conservatives (Ban)"""
    if libdem == ctx.author:
        await ctx.respond("Why would we ban a follower?")
        return
    elif libdem.id == 871399607542882365:
        await ctx.respond("You shan't ban your one true Leader!")
        return
    elif libdem.guild_permissions.administrator:
            await ctx.respond("Sorry, I can't ban an MP. Otherwise John Bercow would shout at us lot")
            return
    else:
        ban_embed = discord.Embed(
            title="The Lib Dem has been Banned!",
            description=f"{libdem.mention} has been removed from this Holy Land of the Conservatives by {ctx.author.mention} because {reason}"
        )
        await ctx.respond(embed=ban_embed)
        await libdem.ban(reason = reason)

@bot.slash_command(guild_ids=[871168657382838292, 827650989070090340, 908816464784552026, 964167989916213318, 880890047962955809])
@commands.has_permissions(ban_members = True)
async def initiation(ctx, newconservative : discord.Member):
    """Allow someone to join back the Conservatives (Unban)"""
    unbanEmbed = discord.Embed(
        description=f"{newconservative.mention} has been brought back into the conservative party!",
        title="Member unbanned!") 
    await ctx.respond(embed=unbanEmbed)
    await ctx.guild.unban(newconservative)
    


@bot.slash_command(guild_ids=[871168657382838292, 827650989070090340, 908816464784552026, 964167989916213318, 880890047962955809])
@commands.has_permissions(manage_messages=True)
async def silencing(ctx, labourvoter : discord.Member, reason : str):
    """Silence a Labour voter (Mute)"""
    if labourvoter == ctx.author:
        await ctx.respond("You vote Lib Dem??? Lies!")
        return
    elif labourvoter.id == 871399607542882365:
        await ctx.respond("bro.")
        return
    elif labourvoter.guild_permissions.administrator:
            await ctx.respond("The council couldn't nor shall vote labour. (You can't mute someone who has the same permissions as you)")
            return
    else:
        guild = ctx.guild
        mutedRole = discord.utils.get(guild.roles, name="Muted")

        if not mutedRole:
            mutedRole = await guild.create_role(name="Muted")
            for channel in guild.channels:
                await channel.set_permissions(mutedRole, speak=False, send_messages=False, read_message_history=True, read_messages=True)
        mute_embed = discord.Embed(
                title="The Labour Voter has been silenced!",
                description=f"{labourvoter.mention} has been muted for 'security reasons' by {ctx.author.mention} because {reason}"
            )
        await ctx.respond(embed=mute_embed)
        await labourvoter.add_roles(mutedRole)
        await labourvoter.send("You've been muted! Until you get unmuted, you won't be able to see any other channels, nor new messages, nor be able to reply to any messages. Try to think about your actions before voting for the Green party :)")




@bot.slash_command(guild_ids=[871168657382838292, 827650989070090340, 908816464784552026, 964167989916213318, 880890047962955809])
@commands.has_permissions(manage_messages=True)
async def unsilence(ctx, victim : discord.Member):
    """Let someone speak for changing their ways (Unmute)"""
    role = discord.utils.get(ctx.guild.roles, name="Muted")
    if role in victim.roles:
        unmute_embed = discord.Embed(
                title="The Labour Voter has been silenced!",
                description=f"{victim.mention} has been unmuted for for correcting their ways, and voting for the Conservatives."
            )
        await ctx.respond(embed=unmute_embed)
        await victim.remove_roles(role)
        await victim.send("Thank you for changing your ways and voting Conservative. For this, you have been forgiven. You may now speak again.")
    else:
        await ctx.respond("This person has not voted UKIP, therefore they are free already")











# Fun

@bot.slash_command(guild_ids=[871168657382838292, 827650989070090340, 908816464784552026, 964167989916213318, 880890047962955809])
async def borisimage(ctx):
    """Send an image that includes our God (Probably)"""
    randImageNum = random.randint(1,6)
    match randImageNum:
        case 1:
            await ctx.respond("This is a selfie I took when I became PM", file=discord.File("RandImage\clown.png"))
        case 2:
            await ctx.respond("Inspirational quote by yours truly", file=discord.File("RandImage\geezerboris.png"))
        case 3:
            await ctx.respond("Me and my pal Trump made a good deal on this day. You can tell because I'm smiling", file=discord.File("RandImage\goodDeal.png"))
        case 4:
            await ctx.respond("I think I should get an anime, I'm quite 'kawaii' in this picture, as the new conservatives say", file=discord.File("RandImage\kawaiiBoris.png"))
        case 5:
            await ctx.respond("Me and all my friends in lockdown", file=discord.File("RandImage\party.png"))
        case 6:
            await ctx.respond("Me and the lads were preparing for the 2019 General election", file=discord.File("RandImage\TheGang.png"))
        case _:
            await ctx.respond("Something broke with the command. Best practice is not to try again!")


@bot.slash_command(guild_ids=[871168657382838292, 827650989070090340, 908816464784552026, 964167989916213318, 880890047962955809])
async def higherup(ctx, initiatee : discord.Member):
    """Become a Higher Up of the Conservatives; Become Bloo."""
    initiation_embed = discord.Embed(
        title=f"{initiatee} has officially joined the higher ups of the Conservatives",
        description=f"How golly jolly is that?"
        )
    initiation_embed.set_image(url=f"https://some-random-api.ml/canvas/blue?avatar={initiatee.avatar}")
    await ctx.respond(embed=initiation_embed)



@bot.slash_command(guild_ids=[871168657382838292, 827650989070090340, 908816464784552026, 964167989916213318, 880890047962955809])
async def ukip_irl(ctx, ukipmember : discord.Member):
    """r/ukip_irl"""
    ukipirl_embed = discord.Embed(
        title=f"{ukipmember} will find out what happens once we know they voted UKIP"
        )
    ukipirl_embed.set_image(url=f"https://some-random-api.ml/canvas/jail?avatar={ukipmember.avatar}")
    await ctx.respond(embed=ukipirl_embed)

bot.run("Uh oh! Token go no brr.")

