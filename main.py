import os
import discord
import json
import requests
import random

from discord.ext import commands

from dotenv import load_dotenv

from bot.botUi import CringeSaveButtonView

load_dotenv()
TOKEN = os.getenv('BOT_TOKEN')
PREFIX = os.getenv('PREFIX')

intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(intents=intents, command_prefix=PREFIX)


@bot.event
async def on_ready():
    print(f"{bot.user} is ready and online!")

@bot.command
async def ping(ctx):
    await ctx.send('Pong!')

@bot.command(help='Roll a die')
async def roll(ctx, dice):
    value = random.randint(1, int(dice))
    await ctx.send(f'Your roll is {str(value)}')

@bot.command(help='Sends the picture of a random cat')
async def cat(ctx):
    response = requests.get('https://cataas.com/cat?json=true')

    json_data = json.loads(response.text)
    cat_id = json_data['_id']
    img = f'https://cataas.com/cat/{cat_id}'

    embed = discord.Embed(color = 0xff9900, title = 'Random Cat')
    embed.set_image(url = img)

    await ctx.send(embed=embed)

@bot.slash_command(name='cringe')
async def test_button(ctx, name, level):
    await ctx.respond(f"Wisdom save from cringe by {name}!", view=CringeSaveButtonView(name, int(level)))


bot.run(TOKEN)