from dotenv import load_dotenv
import discord
from discord.ext import commands
import os

load_dotenv()

botToken = os.getenv("DISCORD_TOKEN")
alvin = int(os.getenv("ALVIN_ID"))
intents = discord.Intents.default()
intents.message_content = True
intents.members = True
bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if any(user.id == alvin for user in message.mentions):
        alvinUser = message.guild.get_member(alvin)
        if alvinUser:
            await message.channel.send(f"Hey :3 {alvinUser.mention}")
    
    await bot.process_commands(message)

@bot.command()
async def getMemberID(ctx, member: discord.Member):
    await ctx.send(f"The ID of {member.display_name} is: {member.id}")

bot.run(botToken)