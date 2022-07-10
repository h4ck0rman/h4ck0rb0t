from discord.ext import commands

# retrieve the token stored in the same directory
TOKEN = open('token', 'r').read().strip()
bot = commands.Bot(command_prefix='&')

# Signifies if the bot is ready 
@bot.event
async def on_ready():
	print('Hack0r is ready...')

bot.run(TOKEN)
