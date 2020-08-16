import discord
import discord.ext.commands


TOKEN = "NzQ0NDc4NDk3Njc3OTAxODU0"+".XzjzoQ.rPLHQYvnT6x8kWvi9CRbtvdkGTU"
bot = discord.ext.commands.Bot(command_prefix = "!")


@bot.command()
async def очистОчка(ctx, arg):
    messages = await ctx.channel.history(limit=9999999).flatten()
    try:
        await ctx.channel.delete_messages(messages)
    except:
        messages = await ctx.channel.history(limit=9999999).flatten()
        for msg in messages:
            try:
                await msg.delete()
            except:
                pass

bot.run(TOKEN)
