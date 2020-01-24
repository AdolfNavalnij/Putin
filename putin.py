import discord
from discord.ext import commands
from time import sleep
from sort2 import sort
from random import randint
from randstr import randstr
import subprocess 

def ping():
    command = ['ping', "-n", '11', "discordapp.com"]

    return subprocess.call(command)

client = discord.Client()
TOKEN = 'NjY1MjU1NDM0OTAyNTY4OTg1.Xhi-Fg.UwN8GbUd1miO-ze9s4QgT70bafA'
bot = commands.Bot(command_prefix='put!') #Bot intialization
@bot.command(pass_context=True)
async def Шо(ctx):
	await ctx.send("@Навальный")
	await ctx.message.delete()
@bot.command(pass_context=True)
async def propoganda(ctx): #asinc bot function
	while True:
		x = randstr(5)
		if x == "putin":
			await ctx.send(x)
			break
	print("""Log:
		command propganda было получено""")
@bot.command(pass_context=True)
async def propoganda_company(ctx,arg):
	for i in range(int(arg)):
		await ctx.send("Навальный лох") #not infinity loop of propoganda)))
		print("""Log:
			command propganda_company работает""")

	print("""Log:
		command propganda_company завершено""")
@bot.command(pass_context=True) #4
async def banan(ctx):
	print("""LOG
		banan было получено""")
	while True:
		await ctx.send("@everyone ЗА ПУТИНА")
	raise NameError("Путин сдох")
@bot.command(pass_context=True)
async def yoptascript(ctx,arg):
	if "ксива.малява" in  arg:
		await ctx.send("Этот код работает нах")
	else:
		while True:
			await ctx.send("")
@client.event
async def on_message(message):
	client.delete_messages(message)
	while False:
		await client.delete_messages(randint(000000000000000000,999999999999999999))
bot.run(TOKEN)
